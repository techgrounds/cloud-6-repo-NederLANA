# Subnetting
A subnet, or subnetwork, is a network inside a network. Subnets make networks more efficient. Through subnetting, network traffic can travel a shorter distance without passing through unnecessary routers to reach its destination.

Subnetting narrows down the IP address to usage within a range of devices.
Because an IP address is limited to indicating the network and the device address, IP addresses cannot be used to indicate which subnet an IP packet should go to. Routers within a network use something called a subnet mask to sort data into subnetworks.

A subnet mask is like an IP address, but for only internal usage within a network. Routers use subnet masks to route data packets to the right place. Subnet masks are not indicated within data packets traversing the Internet — those packets only indicate the destination IP address, which a router will match with a subnet.

**Private vs Public subnet**

The instances in the public subnet can send outbound traffic directly to the Internet via Internet Gateway (IGW), whereas the instances in the private subnet can't. Instead, the instances in the private subnet can access the Internet by using a NAT gateway that resides in the public subnet.

A typical example is a public-facing web application (public subnet), while maintaining back-end servers (private subnets) that aren't publicly accessible.

## Key-terms
[CIDR Notation](

[LAN Network](

[NAT Gateway]


## Assignment
Create a network architecture that meets the following requirements:

a) 1 private subnet that can only be reached from within the LAN. This subnet must be able to connect at least 15 hosts.

b) 1 private subnet that accesses the internet through a NAT gateway. This subnet must be able to connect at least 30 hosts (excluding the NAT gateway).

c) 1 public subnet with an internet gateway. This subnet must be able to connect at least 5 hosts (excluding the internet gateway).

Post the architecture you made including a short explanation in the Github
Example:
![image](https://user-images.githubusercontent.com/4924632/146898965-38fe82cc-48bb-4118-85f7-6af3009e7d0d.png)



### References
https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/

https://www.shellhacks.com/cidr-notation-explained-examples/

https://www.cloudflare.com/learning/network-layer/what-is-a-lan/

https://www.subnet-calculator.com/

https://www.lucidchart.com/pages/network-diagram/how-to-draw-a-network-diagram

https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm

https://www.packetswitch.co.uk/aws-nat-gateway-high-availability/

### Issues


### Results

