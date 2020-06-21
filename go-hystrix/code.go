

// Interface to execute - this will allos us to put fake hystrix
type ExecutorRunFunc func() (result interface{}, err error)

type Executor interface {
    Go(command string, output chan<- interface{}, run ExecutorRunFunc) error
}


// Implment Hystrix Backed Executor
type HystrixExecutor struct {
}

func (e HystrixExecutor) Go(command string, output chan interface{}, run ExecutorRunFunc) error {

    _output := make(chan interface{}, 1)
    errors := hystrix.Go(command, func() (error) {
        result, err := run()
        _output <- result
        if err != nil {
            fmt.Println(err)
        }
        return err
    }, nil)

    select {
    case out := <-_output:
        output <- out
        return nil

    case err := <-errors:
    	// If error then we close channel so the client will get null
        close(output)       
        return err
    }
}



// No Op executor

type FakeHystrixExecutor struct {
}

func (e FakeHystrixExecutor) Go(command string, output chan interface{}, run ExecutorRunFunc) error {
    result, err := run()
    output <- result
    return err
}




// Configure and use Hystrix command
hystrix.ConfigureCommand("my_command", hystrix.CommandConfig{
    Timeout:               5,
    MaxConcurrentRequests: 100,
    ErrorPercentThreshold: 25,
})

executor := HystrixExecutor{}


output := make(chan interface{}, 1)
executor.Go(
    "my_command",
    output,
    func() (interface{}, error) {
        res, i := HiService() // your code here
        var err error = nil
        if i == 500 {
            err = errors.New("Got 500 in " + string(i))
        }
        return res, err
    },
)
result := <-output


