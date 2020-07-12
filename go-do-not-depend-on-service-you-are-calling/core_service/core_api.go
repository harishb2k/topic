package core_service

// This is a internal service API
type coreApi struct {
    key   string
    value string
}

// A method which we want client to use
func (c *coreApi) GetModifiedKey() string {
    return c.getKeyInternal()
}

func (c *coreApi) getKeyInternal() string {
    return c.key + "_" + c.value
}

// This is a constructor which is exposed to outside world
// NOTE - nothing from this file is exposed
// Event if "GetModifiedKey" is public it cannot be accessed because it is attached to private "coreApi"
func NewCoreApi(key string, value string) *coreApi {
    return &coreApi{
        key:   key,
        value: value,
    }
}


