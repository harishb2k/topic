Here our client needs to call core service. But we ensured that we do not depend on core service.

This gives a way to replace the core service and we will have very small code change on client.


Now why we did not created a interface in core service?
	We created interface on client. Think if we need to use new core serivce then the core service has to implement this interface method.

	But if I had used a interface from core service 1 then I would always have to depend on core service 1, even if I use core service 2


Where this desing is used:

AWS CNI pluing uses it. Today they client uses AWS SDK and linux net link lib. But if AWS CNI (clinet of AWS sdk and net link) wants to use something
else then it can use it. 
 

	 
