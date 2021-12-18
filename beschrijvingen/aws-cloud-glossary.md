

### Stateful firewall 
-monitor all aspects of the traffic streams, their characteristics and communication channels. These firewalls can integrate encryption or tunnels, identify TCP connection stages, packet state and other key status updates.

### Stateless firewall
-one of the earlier iterations of firewalls, stateless only focus on individual packets, using preset rules to filter traffic, and often does not look beyond packet headers to decide if it might be truly desired communications. Is cheaper and can handle high traffic.

### Inherited Controls
– Controls which a customer fully inherits from AWS.
* Physical and Environmental controls

### Shared Controls
– Controls which apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services. Examples include:

* Patch Management – AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.

* Configuration Management – AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.

* Awareness & Training - AWS trains AWS employees, but a customer must train their own employees.

### Customer Specific Controls
– Controls which are solely the responsibility of the customer based on the application they are deploying within AWS services. Examples include:

* Service and Communications Protection or Zone Security which may require a customer to route or zone data within specific security environments.
