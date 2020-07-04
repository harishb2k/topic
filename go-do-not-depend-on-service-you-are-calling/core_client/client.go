package core_client

import (
    "awesomeProject/core_service"
    "fmt"
)

type CoreApi interface {
    // NOTE - this method is same as the method which is defined by private "coreApi"
    GetModifiedKey() string
}

func CoreApiUser() {
    var ca CoreApi

    // Note we would get a result of private "coreApi" but it implements our
    // "CoreApi" interface
    // This is a reverse way of DI
    // This helps us to avoid depending on package from core service
    ca = core_service.NewCoreApi("key_1", "value_1")

    fmt.Println(ca.GetModifiedKey())
}


