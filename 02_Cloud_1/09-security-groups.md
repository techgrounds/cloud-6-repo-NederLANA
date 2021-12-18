# Security Groups
Security Groups are stateful virtual firewalls that can be assigned to instances. They do not run in the OS, but rather in the VPC.

One Security Group can be assigned to multiple instances. The other way around, one instance can have up to 5 Security Groups.

Security Groups only have allow rules. Everything not explicitly allowed is automatically implicitly denied.

A Network Access Control List (NACL) is a stateless firewall that runs on the subnet level in a VPC.
A NACL has both explicit allow and deny rules. Rules have a number assigned to them. This number indicates the order in which the rules are applied.

By default, a NACL is configured to allow all traffic in and out of the network.

![op9-nacl-vs-securitygrp](https://user-images.githubusercontent.com/4924632/146643719-f7d7df83-ce49-4024-b58e-15be544b7cbf.png)

**You can secure your instances using only security groups. However, you can add network ACLs as an additional layer of defense.**

![image](https://user-images.githubusercontent.com/4924632/146643740-67301daa-4d3f-464d-a784-43d785db5120.png)


## Key-terms
[Stateful firewall](https://github.com/techgrounds/cloud-6-repo-NederLANA/blob/ceaacbca7f5efb137fd0ff5e477015074d10b4bf/beschrijvingen/aws-cloud-glossary.md#stateful-firewall)

[Stateless firewall](https://github.com/techgrounds/cloud-6-repo-NederLANA/blob/ceaacbca7f5efb137fd0ff5e477015074d10b4bf/beschrijvingen/aws-cloud-glossary.md#stateless-firewall)

## Opdracht

Study:
Security Groups in AWS
Network Access Control Lists in AWS

### Gebruikte bronnen
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html#VPC_Security_Comparison


### Ervaren problemen


### Resultaat

