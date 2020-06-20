

type Server struct {
    Type                   string `yaml:"type"`
    ApplicationContextPath string `yaml:"applicationContextPath"`
    AdminContextPath       string `yaml:"adminContextPath"`
    Connector              struct {
        Port int    `yaml:"port"`
        Type string `yaml:"type"`
    } `yaml:"connector"`
}

type LockConfig struct {
    LockExpiryTimeInMs  int  `yaml:"lockExpiryTimeInMs"`
    LockTryWaitTimeInMs int  `yaml:"lockTryWaitTimeInMs"`
    IgnoreLockError     bool `yaml:"ignoreLockError"`
}

type DistributedLockConfig struct {
    LockConfigsExt map[string]LockConfig `yaml:"lockConfigs"`
}

// This is the top Json object
type Config struct {
    Server                Server                `yaml:"server"`
    DistributedLockConfig DistributedLockConfig `yaml:"distributedLockConfig"`
}


service := server.Config{}
data, err := ioutil.ReadFile("app.yml")
err = yaml.Unmarshal(data, &service)

