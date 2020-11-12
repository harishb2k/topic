```java
when(mockObject.callSync(
                ArgumentMatchers.argThat(call -> {
                    return Objects.equals(call.getServer(), "myServer") && Objects.equals(call.getApi(), "myApi");
                })
        )).thenReturn(someMockResponse);
```
