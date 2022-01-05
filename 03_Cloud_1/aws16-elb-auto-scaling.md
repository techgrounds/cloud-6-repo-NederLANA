# Elastic Load Balancing and Auto Scaling
One of the main advantages of the cloud is that you don’t need to guess how much capacity you need. You can always scale up and down with on-demand services. One of the services that enables this is called Auto Scaling.

When you run an application with a spiky workload, you can host the application on a fleet of EC2 instances instead of a single server. When the demand for the application is high, Auto Scaling can automatically add instances to the fleet. When the demand is lower, it can similarly remove instances.

To make sure all servers are the same, Auto Scaling makes use of a (custom) AMI. Auto Scaling makes use of CloudWatch metrics to determine whether to add or remove instances.

In a traditional architecture, a client connects to a single server with a single IP address. When dealing with a fleet of servers, this would not work. Therefore, a load balancer can be introduced as a connection endpoint for the client. The load balancer will forward the request to one of the servers in the fleet, and relay the response back to the client.

AWS’ ELB services is a managed service that provides load balancing to a fleet of instances. There are two types of ELBs:

* Application Load Balancer: this ELB works using HTTP and HTTPS protocols (layer 7 of the OSI stack).
* Network Load Balancer: this ELB works using TCP and UDP (layer 4 of the OSI stack).


## Key-terms


## Assignment

This lab walks you through using the Elastic Load Balancing (ELB) and Auto Scaling services to load balance and automatically scale your infrastructure.

* **Elastic Load Balancing** automatically distributes incoming application traffic across multiple Amazon EC2 instances. It enables you to achieve fault tolerance in your applications by seamlessly providing the required amount of load balancing capacity needed to route application traffic.

* **Auto Scaling** helps you maintain application availability and allows you to scale your Amazon EC2 capacity out or in automatically according to conditions you define. You can use Auto Scaling to help ensure that you are running your desired number of Amazon EC2 instances. Auto Scaling can also automatically increase the number of Amazon EC2 instances during demand spikes to maintain 
performance and decrease capacity during lulls to reduce costs. Auto Scaling is well suited to applications that have stable demand patterns or that experience hourly, daily, or weekly variability in usage.

**Objectives**

After completing this lab, you can:

Create an Amazon Machine Image (AMI) from a running instance.

Create a load balancer.

Create a launch template and an Auto Scaling group.

Automatically scale new instances within a private subnet.

Create Amazon CloudWatch alarms and monitor performance of your infrastructure.


### References
https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg.html

https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html


### Issues

Upgrade to new EC2 Experience?

![image](https://user-images.githubusercontent.com/4924632/147222615-14bc0085-b213-4555-9f10-3928ed7c31a2.png)



### Results

**Exercise 1:**

Create AMI from EC2

![image](https://user-images.githubusercontent.com/4924632/147221099-39828501-2263-47d2-b82d-95ff3422c99d.png)

![image](https://user-images.githubusercontent.com/4924632/147221958-a23096e9-acb4-4d9e-ab8f-ff66c18ea1bb.png)

**Exercise 2:**

Create an application load balancer:

![image](https://user-images.githubusercontent.com/4924632/147225877-7f6d256e-e701-4101-895a-7989f602381e.png)

![image](https://user-images.githubusercontent.com/4924632/147223419-cad6a9e7-708c-4027-97ea-54183767b494.png)

![image](https://user-images.githubusercontent.com/4924632/147225543-85221b38-d0fc-4631-acce-c592c1f906e6.png)

4) Test the load balancer
*unable to test load balancer with load DNS*
*was able to check load for instance*

![image](https://user-images.githubusercontent.com/4924632/147226620-7fd136b3-f6aa-40c0-abc5-6b216cf18e64.png)


**Exercise 3:**
Create launch configuration for an auto scaling group

![image](https://user-images.githubusercontent.com/4924632/147229866-aff5dfa9-3d90-4cda-91a3-d23ea322477b.png)

![image](https://user-images.githubusercontent.com/4924632/147230717-7890a645-7a00-44f3-8b19-a070e6aa7a87.png)

![image](https://user-images.githubusercontent.com/4924632/147231004-45fb1cd2-b0e4-4b8c-a249-7aae523c4a17.png)

**Exercise 4:**

Verify EC2 instances are online (OG 16 is original, plus 2 more from autoscaling

![image](https://user-images.githubusercontent.com/4924632/147232101-dc92a815-9f0a-4723-9dae-8663a8a942e7.png)


Access server via the ELB DNS returns an error: 504 Gateway time-out









