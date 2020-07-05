
// instrumentedInterface wraps the Interface and records the operations and errors metrics.
type instrumentedInterface struct {
	client Interface
}

// NewInstrumentedInterface creates an instrumented Interface from an existing Interface.
func NewInstrumentedInterface(dockerClient Interface) Interface {
	return instrumentedInterface{
		client: dockerClient,
	}
}

// recordOperation records the duration of the operation.
func recordOperation(operation string, start time.Time) {
	metrics.DockerOperations.WithLabelValues(operation).Inc()
	metrics.DockerOperationsLatency.WithLabelValues(operation).Observe(metrics.SinceInSeconds(start))
}

// recordError records error for metric if an error occurred.
func recordError(operation string, err error) {
	if err != nil {
		if _, ok := err.(operationTimeout); ok {
			metrics.DockerOperationsTimeout.WithLabelValues(operation).Inc()
		}
		// Docker operation timeout error is also a docker error, so we don't add else here.
		metrics.DockerOperationsErrors.WithLabelValues(operation).Inc()
	}
}


func (in instrumentedInterface) ListContainers(options dockertypes.ContainerListOptions) ([]dockertypes.Container, error) {
	const operation = "list_containers"
	defer recordOperation(operation, time.Now())

	out, err := in.client.ListContainers(options)
	recordError(operation, err)
	return out, err
}


