# Elastic Block Stores (EBS)
EBS can be seen as virtual hard drives in the cloud. They can be either root volumes (like an internal hard disk), or seperate volumes (like an external hard disk). One instance of an EBS is called a volume. One volume can be attached to only one EC2 instance at a time, although for every non-root volume, you can detach it and attach it to a different EC2 instance.You can create snapshots of a volume to create backups or new identical volumes. These snapshots will be stored in S3.
There are four different volume types. Generally speaking, lower performance means lower cost.

For security, EBS volumes can be encrypted. **Volumes can be scaled up, but not down**.
Any external device, including EBS, needs to be mounted if you want to use them in Linux.


## Key-terms

**EBS mount**

**EBS snapshot**

Amazon EBS volumes deliver the following features:

* Persistent storage: Volume lifetime is independent of any particular Amazon EC2 instance.
* General purpose: Amazon EBS volumes are raw, unformatted block devices that can be used from any operating system.
* High performance: Amazon EBS volumes are equal to or better than local Amazon EC2 drives.
* High reliability: Amazon EBS volumes have built-in redundancy within an Availability Zone.
* Designed for resiliency: The AFR (Annual Failure Rate) of Amazon EBS is between 0.1% and 1%.
* Variable size: Volume sizes range from 1 GB to 16 TB.
* Easy to use: Amazon EBS volumes can be easily created, attached, backed up, restored, and deleted.

## Opdracht
**This lab focuses on Amazon Elastic Block Store (Amazon EBS), a key underlying storage mechanism for Amazon EC2 instances. In this lab, you will learn how to create an Amazon EBS volume, attach it to an instance, apply a file system to the volume, and then take a snapshot backup.**

By the end of this lab, you will be able to:

Create an Amazon EBS volume
Attach and mount your volume to an EC2 instance
Create a snapshot of your volume
Create a new volume from your snapshot
Attach and mount the new volume to your EC2 instance

--------------
**Exercise 1:**

Start your sandbox lab and open the AWS console.
Navigate to the EC2 menu.
Create a t2.micro Amazon Linux 2 machine with all the default settings (the key can be downloaded from the sandbox lab)
Create a new EBS volume with the following requirements:
Volume type: General Purpose SSD (gp2)
Size: 1 GiB
Availability Zone: same as your EC2
Wait for its state to be available.

**Exercise 2:**

Attach your new EBS volume to your EC2 instance.
Connect to your EC2 instance using SSH.
Mount the EBS volume on your instance.
Create a text file and write it to the mounted EBS volume.

**Exercise 3:**

Create a snapshot of your EBS volume.
Remove the text file from your original EBS volume.
Create a new volume using your snapshot.
Detach your original EBS volume.
Attach the new volume to your EC2 and mount it.
Find your text file on the new EBS volume.



### Gebruikte bronnen
https://aws.amazon.com/ebs/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html

Connecting via SSH putty to EC2: 
https://www.youtube.com/watch?v=f52IOtTqcP8



### Ervaren problemen


### Resultaat

![image](https://user-images.githubusercontent.com/4924632/146375227-87a4c1f0-0469-4a59-89af-cd56495d620a.png)

**Exercise 1: Launch EC2. Add new EBS volume of 1GiB*

![op7-ex1-new-ebsvolume](https://user-images.githubusercontent.com/4924632/146378451-7377d903-0c2e-44fb-a9e2-040588af1a67.png)

**Exercise 2: Attach & Mount new EBS to EC2 via SSH. Create text file and mount EC2.

![op7-ex2-attach-EBS1-EC2](https://user-images.githubusercontent.com/4924632/146380108-dd360212-dc55-44ba-b52f-893c2064b011.png)





