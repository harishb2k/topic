## Helix base setup
Helix setup need following setup
1. Cluster set-up
2. Resource setup
3. Register yourself as participant
4. Register yourself as controller

#### Cluster set-up
We need to have a cluster to work with Helix. Only problem we face is bootstrap (only one node need to create cluster)
 
```java
ZKHelixAdmin admin = new ZKHelixAdmin.Builder().setZkAddress(ZK_ADDRESS).build();

// Step 1 - you need to create a cluster first
// We get error if we already have a cluster with same name 
//    - we can check and create using following 
String cluster = admin.getClusters().stream().filter(s -> Objects.equals(s, CLUSTER_NAME)).findFirst().orElse(null);
if (Strings.isNullOrEmpty(cluster)) {
    admin.addCluster(CLUSTER_NAME, false);
}


// Step 2 - You need to create information about your node
// This is done by creating a InstanceConfig. Put correct host and port here.
InstanceConfig instanceConfig = new InstanceConfig("localhost_" + port);
instanceConfig.setHostName("localhost");
instanceConfig.setPort("" + port);
instanceConfig.setInstanceEnabled(true);

// Add instance to cluster
admin.addInstance(CLUSTER_NAME, instanceConfig);

```

#### Resource setup
A resource can be anything. It is divided in N partitions, and these partitions are then assigned to
nodes. A resource and partitions is a virtual resource, there is nothing backing this resource.
It is created for Helix to do the assignment.  
```java
int NUM_PARTITIONS = 6;
int NUM_REPLICAS = 1;

// Step 1 - Create a resource if it does not exist already
String resource = admin.getResourcesInCluster(CLUSTER_NAME).stream().filter(s -> Objects.equals(RESOURCE_NAME, s)).findFirst().orElse(null);
if (Strings.isNullOrEmpty(resource)) {
    StateModelDefinition myStateModel = defineStateModel();   
    admin.addStateModelDef(CLUSTER_NAME, STATE_MODEL_NAME, myStateModel);
    admin.addResource(CLUSTER_NAME, RESOURCE_NAME, NUM_PARTITIONS, STATE_MODEL_NAME, "FULL_AUTO");
}
```

###### Re-balance 
You need to initiate re-balance for partition re-allocation. 
When you boot the first node, it is going to fail because you will not have enough replica. To overcome
this problem you may have to run a busy loop to ensure re-balance is called.
```java
 while (true) {
    try {
        admin.rebalance(CLUSTER_NAME, RESOURCE_NAME, NUM_REPLICAS);
        break;
    } catch (Exception e) {
        System.out.println("Do not have enough replica..." + e.getMessage());
    }
    Thread.sleep(1000);
}
```

#### Register yourself as participant
You need to make yourself as participant - a participant will be allocated partition. It is just a logical
participant and logical partition. 
```java
manager = HelixManagerFactory.getZKHelixManager(
            Application.CLUSTER_NAME,
            instanceConfig.getInstanceName(),
            InstanceType.PARTICIPANT,
            Application.ZK_ADDRESS
    );

MasterSlaveStateModelFactory stateModelFactory = new MasterSlaveStateModelFactory(instanceConfig.getInstanceName());
StateMachineEngine stateMach = manager.getStateMachineEngine();
stateMach.registerStateModelFactory(Application.STATE_MODEL_NAME, stateModelFactoryNew);
manager.connect();
```

#### Register yourself as controller
```java
// Step 2 - register your-self as controller 
controler = HelixControllerMain.startHelixController(
                Application.ZK_ADDRESS,
                Application.CLUSTER_NAME,
                "localhost_9100",
                HelixControllerMain.STANDALONE
        );
``` 

## Handling state transaction 
Helix does not know what it means to go from online to offline OR making master to slave. It using the StateModelFactory
to do the actual work 
```java

// Step 1 - Set state handling in manager
OnlineOfflineStateModelFactoryNew stateModelFactoryNew = new OnlineOfflineStateModelFactoryNew();
stateMach.registerStateModelFactory(Application.STATE_MODEL_NAME, stateModelFactoryNew);

// Step 2 - your application logic
class OnlineOfflineStateModelFactoryNew extends StateModelFactory<StateModel> {
    @Override
    public StateModel createNewStateModel(String stateUnitKey) {
        OnlineOfflineStateModel stateModel = new OnlineOfflineStateModel();
        return stateModel;
    }

    @StateModelInfo(states = "{'MASTER','SLAVE'}", initialState = "OFFLINE")
    public static class OnlineOfflineStateModel extends StateModel {
        
        @Transition(from = "SLAVE", to = "MASTER")
        public void onBecomeOnlineFromOffline(Message message,NotificationContext context) {
            System.out.println("SLAVE_MASTER");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            ////////////////////////////////////////////////////////////////////////////////////////////////
            // Application logic to handle transition  - When a partition goes to MASTER from SLAVE       //           
            ////////////////////////////////////////////////////////////////////////////////////////////////
        }

        @Transition(from = "MASTER", to = "SLAVE")
        public void MASTERSLAVE(Message message, NotificationContext context) {
            System.out.println("MASTER_SLAVE");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            ////////////////////////////////////////////////////////////////////////////////////////////////
            // Application logic to handle transition  - When a partition goes to SLAVE from MASTER       //           
            ////////////////////////////////////////////////////////////////////////////////////////////////
        }

        @Transition(from = "OFFLINE", to = "SLAVE")
        public void OFFLINE_SLAVE(Message message, NotificationContext context) {
            System.out.println("OFFLINE_SLAVE");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            ////////////////////////////////////////////////////////////////////////////////////////////////
            // Application logic to handle transition  - When a partition goes to SLAVE from OFFLINE      //           
            ////////////////////////////////////////////////////////////////////////////////////////////////
        }

        @Transition(from = "SLAVE", to = "OFFLINE")
        public void SLAVE_OFFLINE(Message message, NotificationContext context) {
            System.out.println("SLAVE_OFFLINE");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            ////////////////////////////////////////////////////////////////////////////////////////////////
            // Application logic to handle transition  - When a partition goes to OFFLINE from SLAVE      //           
            ////////////////////////////////////////////////////////////////////////////////////////////////
        }

        @Transition(from = "OFFLINE", to = "DROPPED")
        public void OFFLINE_DROPPED(Message message, NotificationContext context) {
            System.out.println("OFFLINE_DROPPED");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            ////////////////////////////////////////////////////////////////////////////////////////////////
            // Application logic to handle transition  - When a partition goes to DROPPED from OFFLINE    //           
            ////////////////////////////////////////////////////////////////////////////////////////////////
        }
    }
}
```

## Miscellaneous
#### Jvm hook to de-register when nodes goes down
When node goes down then we can register jvm hook to de-register node. This will kick-in the re-balance asap.
Otherwise it takes some time for helix to do re-balance
```java
Runtime.getRuntime().addShutdownHook(new Thread(() -> {    
         controler.disconnect();
         manager.disconnect();
    }));
``` 
#### Timeouts 
When a node is killed and JVM shudtown hook does not run, then it takes (default=1 min) for Helix to
start re-balance
You can configure it by yourself.
```java
// Set timeouts to 5 sec
System.setProperty(SystemPropertyKeys.ZK_CONNECTION_TIMEOUT, 5000 + "");
System.setProperty(SystemPropertyKeys.ZK_SESSION_TIMEOUT, 5000 + "");
```
