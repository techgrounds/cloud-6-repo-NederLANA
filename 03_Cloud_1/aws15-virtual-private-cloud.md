# Virtual Private Cloud (VPC)
Amazon VPC is typically described as a virtual private data center in the cloud. With a VPC you have full control over the design of the network. You can create subnets, internet gateways (igw), NAT gateways, VPN connections, and more.

There is always a default VPC when you create a new AWS account, but you can add up to 5 non-default VPCs per region per account. This is a soft limit; you can request the limit to be raised.
Many services, like EC2, RDS and ECS require a VPC to be placed into.

When you create a VPC, you must assign a CIDR block, which cannot be changed after creation. So choose your CIDR block and subnet mask carefully, as they have to allow for enough subnets and hosts.

Subnets can be either public or private. The only difference is that private subnets do not have an entry for the internet gateway (igw) in their route table, where public subnets do. In other words, private subnets cannot access the internet without a NAT gateway or a NAT instance.

VPCs operate at the regional level, while subnets can only be placed into a single Availability Zone.

Elastic IPs are also available from the VPC menu. EIPs are public IP addresses that can be dynamically allocated to resources like EC2 instances or NAT gateways.

In this lab, you will use Amazon Virtual Private Cloud (VPC) to create your own VPC and add additional components to produce a customized network. You will also create security groups for your EC2 instance. You will then configure and customize an EC2 instance to run a web server and launch it into the VPC.
Amazon Virtual Private Cloud (Amazon VPC) enables you to launch Amazon Web Services (AWS) resources into a virtual network that you defined. This virtual network closely resembles a traditional network that you would operate in your own data center, with the benefits of using the scalable infrastructure of AWS. You can create a VPC that spans multiple Availability Zones.

After completing this lab, you can:
Create a VPC.
Create subnets.
Configure a security group.
Launch an EC2 instance into a VPC.

## Key-terms
[RDS](

[ECS](

[CIDR](

[EIP](

## Assignment

1) Build this infrastructure in AWS:

![image](https://user-images.githubusercontent.com/4924632/147114203-079b258f-f62c-4545-b031-bcc2da3f4d5e.png)

2) Launch an EC2 instance into the VPC.


### References
https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#VPC_Launch_Instance

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html#add-rule-authorize-access

### Issues
**EC2 unable to connect**

1) Error message: Port 22 needs to be open for AMI to access

![image](https://user-images.githubusercontent.com/4924632/147173354-e8153dba-6842-48be-b64f-2997b09ecc71.png)

Solution, reconfigure security group to allow SSH inbound via port 22.

![image](https://user-images.githubusercontent.com/4924632/147173975-44ff5371-f826-4cf3-895b-e20bc3f13b60.png)

2) ECS unable to connect (via console). *Assignment was to connect via DNS*

(Had to enable public IP for EC2, so associated new elastic IP to the instance)

**unresolved**(might be this issue)

![image](https://user-images.githubusercontent.com/4924632/147211860-d83e0274-0867-48d4-a13b-c51d618e2edc.png)


### Results

**Exercise 1:** Configuration

![image](https://user-images.githubusercontent.com/4924632/147169807-9b502261-2e36-4267-8c27-15b3f748c6c6.png)

Elastic IP address allocated 

![image](https://user-images.githubusercontent.com/4924632/147166072-4be0ed60-f417-4e4b-872f-84a6e210385e.png)

lab vpc created with private and public (with NAT) subnet created in AZ 1a:

![image](https://user-images.githubusercontent.com/4924632/147170075-5eb58850-e476-4565-9516-a24981d66371.png)

**Exercise 2:**
In same VPC, create Public and private subnet 2 in AZ 1b:

![image](https://user-images.githubusercontent.com/4924632/147170526-d1a22783-6719-4e36-a420-e1cd683f89aa.png)

Associate Private Route Table (main) to Private subnet1 and Private subnet2

![image](https://user-images.githubusercontent.com/4924632/147171139-9bac8422-e00a-42bb-ae8e-e2f422b0f1fb.png)

Associate Public Route Table (other) to Public subnet1 and Public subnet2

![image](https://user-images.githubusercontent.com/4924632/147171321-81ed4f4e-b5c9-4374-bd40-43abca3cd749.png)

**Exercise 3:**
Create Security Group to enable HTTP access

![image](https://user-images.githubusercontent.com/4924632/147171857-e00c74a1-a3ea-49a0-8f0f-79ea661fcac1.png)

**Exercise 4:**
Launch EC2 instance (Linux)

![image](https://user-images.githubusercontent.com/4924632/147173498-acf2b2cf-b0ae-4d34-9c49-c3406e0e52e2.png)

Connect to Web server using public IPv4 DNS name:

![image](https://user-images.githubusercontent.com/4924632/147212829-cb4bdc7a-9df5-44fc-8ea6-5db069f8976a.png)





