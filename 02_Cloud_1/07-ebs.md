# Elastic Block Stores (EBS)
EBS can be seen as virtual hard drives in the cloud. They can be either root volumes (like an internal hard disk), or seperate volumes (like an external hard disk). One instance of an EBS is called a volume. One volume can be attached to only one EC2 instance at a time, although for every non-root volume, you can detach it and attach it to a different EC2 instance.You can create snapshots of a volume to create backups or new identical volumes. These snapshots will be stored in S3.

There are four different volume types. Generally speaking, lower performance means lower cost.

For security, EBS volumes can be encrypted. **Volumes can be scaled up, but not down**.
Any external device, including EBS, needs to be mounted if you want to use them in Linux.


## Key-terms

**EBS mount**

**EBS snapshot**

**Amazon EBS volumes deliver the following features:**

* Persistent storage: Volume lifetime is independent of any particular Amazon EC2 instance.

* General purpose: Amazon EBS volumes are raw, unformatted block devices that can be used from any operating system.

* High performance: Amazon EBS volumes are equal to or better than local Amazon EC2 drives.

* High reliability: Amazon EBS volumes have built-in redundancy within an Availability Zone.

* Designed for resiliency: The AFR (Annual Failure Rate) of Amazon EBS is between 0.1% and 1%.

* Variable size: Volume sizes range from 1 GB to 16 TB.

* Easy to use: Amazon EBS volumes can be easily created, attached, backed up, restored, and deleted.

* **An EBS volume is off-instance storage that can persist independently from the life of an instance. You continue to pay for the volume usage as long as the data persists. So delete the EBS you no longer use!!!**

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

ex 2: 

editing route table (first create internet gateway):
https://www.youtube.com/watch?v=6h13JGeiE2Y

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#vpc-igw-internet-access

https://devopscube.com/mount-ebs-volume-ec2-instance/

creating files in mounted dir:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

**Ex3:**

create a snapshot: 
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html

create volume from a snapshot:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html#ebs-create-volume-from-snapshot


### Ervaren problemen


### Resultaat

![image](https://user-images.githubusercontent.com/4924632/146375227-87a4c1f0-0469-4a59-89af-cd56495d620a.png)

**Exercise 1: Launch EC2. Add new EBS volume of 1GiB*

![op7-ex1-new-ebsvolume](https://user-images.githubusercontent.com/4924632/146378451-7377d903-0c2e-44fb-a9e2-040588af1a67.png)

**Exercise 2: Attach & Mount new EBS to EC2 via SSH. Create text file and mount EC2.

Attach new EBS volume to ec2 instance
![op7-ex2-attach-EBS1-EC2](https://user-images.githubusercontent.com/4924632/146380108-dd360212-dc55-44ba-b52f-893c2064b011.png)

Connect to EC2 using SSH
![op7-ex2-ssh-connect-ec2](https://user-images.githubusercontent.com/4924632/146527347-f411e1e5-f9df-4cd7-99b7-ca4d30e6834b.png)

Mount EBS volume on EC2
![op7-ex2-mount-newvolume-ec2](https://user-images.githubusercontent.com/4924632/146532878-f2461866-40ed-49ed-868e-979ead9220b3.png)

Write text file to the mounted EBS volume
![op-ex2-write-text-mounted-EBS](https://user-images.githubusercontent.com/4924632/146536909-6b4c4b73-79bb-405b-9355-082476a929e2.png)

**Exercise 3: Create EBS snapshot, remove text.txt, create new volume from snapshot, detach original EBS, attach new volume and mount it. Find text.txt on new EBS.

Create snapshot of EBS volume (1G volume)
![op7-ex3-ec2-snapshot](https://user-images.githubusercontent.com/4924632/146548842-351218f6-e18a-4cdb-ae9e-684f7a16427b.png)

Remove the text file from your original EBS volume.

Create another new volume using your snapshot.
![op7-ex3-2Gvolume-from-snapshot](https://user-images.githubusercontent.com/4924632/146551302-074c1b8e-a0c1-4b19-90fd-4b34bc31bc2c.png)


Detach your original EBS volume.
![op7-ex3-detach-original-ebs](https://user-images.githubusercontent.com/4924632/146551748-03f8f8dc-b2dc-4238-96f1-49457ae46949.png)

Attach the new volume to your EC2 and mount it.
![op7-ex3-attach-mount-newvolume2](https://user-images.githubusercontent.com/4924632/146555933-4aa6712d-651f-4fc0-afc1-15ba5d70da51.png)

Find your text file on the new EBS volume.
![op7-ex3-find-old-text-new-ebs](https://user-images.githubusercontent.com/4924632/146556209-982cc0f9-8f00-4066-b8a1-578b67a6215f.png)





