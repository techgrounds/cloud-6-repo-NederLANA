# Elastic File System EFS
Amazon Elastic File System (EFS) automatically grows and shrinks as files are added or removed.

With Amazon EFS:
1) create a file system

2) mount the file system on an Amazon EC2 instance

3)  read and write data to and from the file system.

![elastic-file-system](04_Cloud_2/elastic-file-system.md)

**Features of EFS:**
* Amazon EFS file systems using Standard storage classes store data and metadata across multiple Availability Zones in an AWS Region. 

* can grow to petabyte scale, drive high levels of throughput, and allow massively parallel access from compute instances to the data.

* provides file system access semantics, such as strong data consistency and file locking. 

* enables control access to file systems through Portable Operating System Interface (POSIX) permissions. 

* supports authentication, authorization, and encryption capabilities to help meet security and compliance requirements.Supports two forms of encryption for file systems, encryption in transit and encryption at rest. 

Range of storage classes for different use cases:
* **EFS standard storage class** - regtional storage class for frquently accessed data.
* **EFS infrequent access** - regional storage class for infrequently accessed files.

* **EFS One Zone (and One Zone-IA)** - lower cost storage within a single Availability Zone in an AWS Region.


## Key-terms
[Mount Target](../beschrijvingen/aws-cloud-glossary.md#mount-target)

[Access Points](../beschrijvingen/aws-cloud-glossary.md#access-points)

[Security Groups](../beschrijvingen/aws-cloud-glossary.md#security-groups)

## Assignment

In this Getting Started exercise, you can learn how to quickly create an Amazon Elastic File System (Amazon EFS) file system. As part of this process, you mount your file system on an Amazon Elastic Compute Cloud (Amazon EC2) instance in your virtual private cloud (VPC). You also test the end-to-end setup.

1) Create your Amazon EFS file system.

2) Create your Amazon EC2 resources, launch your instance, and mount the file system.

3) Transfer files to your EFS file system using AWS DataSync.

4) Clean up your resources and protect your AWS account.

### References
https://aws.amazon.com/efs/

https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html

https://docs.aws.amazon.com/efs/latest/ug/getting-started.html

### Issues


### Results

1) Open the Amazon EFS Management Console to create a file system https://console.aws.amazon.com/efs/

[](../00_includes/wk04/efs-created.png)

2) 