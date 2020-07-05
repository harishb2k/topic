Here we can see that we want to expose Interface which will give a DockerEngineInterface=kubeDockerClient.

kubeDockerClient has not metrics, and it is pure class.

Now instead of puting the logic in kubeDockerClient we created instrumentedInterface.

type instrumentedInterface struct {
	client Interface
}

All methods are implemented and do the logging. This makes the kube client a pure client code. 