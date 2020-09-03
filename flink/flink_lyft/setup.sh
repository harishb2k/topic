
# This is basic 
kubectl create -f https://raw.githubusercontent.com/lyft/flinkk8soperator/v0.5.0/deploy/crd.yaml
kubectl create -f https://raw.githubusercontent.com/lyft/flinkk8soperator/v0.5.0/deploy/namespace.yaml
kubectl create -f https://raw.githubusercontent.com/lyft/flinkk8soperator/v0.5.0/deploy/role.yaml
kubectl create -f https://raw.githubusercontent.com/lyft/flinkk8soperator/v0.5.0/deploy/role-binding.yaml

kubectl create -f https://raw.githubusercontent.com/lyft/flinkk8soperator/v0.5.0/deploy/config.yaml

https://raw.githubusercontent.com/harishb2k/topic/master/flink/flink_lyft/flinkk8soperator.yaml
kubectl get pods -n flink-operator

https://raw.githubusercontent.com/harishb2k/topic/master/flink/flink_lyft/flink-operator-custom-resource.yaml
kubectl get deployments -n flink-operator
kubectl get flinkapplication.flink.k8s.io -n flink-operator wordcount-operator-example -o yaml
