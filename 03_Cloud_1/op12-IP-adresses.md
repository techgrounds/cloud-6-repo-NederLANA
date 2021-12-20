# IP Addresses
The internet needs a way to differentiate between different computers, routers, and websites. An IP address is a unique address that identifies a device on the internet or a local network. IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network. In essence, IP addresses are the identifier that allows information to be sent between devices on a network: they contain location information and make devices accessible for communication.

**What is an IP?**

An IP address is a string of numbers separated by periods. IP addresses are expressed as a set of four numbers — an example address might be 192.158.1.38. Each number in the set can range from 0 to 255. So, the full IP addressing range goes from 0.0.0.0 to 255.255.255.255.

IP addresses are not random. They are mathematically produced and allocated by the Internet Assigned Numbers Authority (IANA), a division of the Internet Corporation for Assigned Names and Numbers (ICANN), established in the United States in 1998 to help maintain the security of the internet and allow it to be usable by all. Each time anyone registers a domain on the internet, they go through a domain name registrar, who pays a small fee to ICANN to register the domain.

**How do IP addresses work**

If you want to understand why a particular device is not connecting in the way you would expect or you want to troubleshoot why your network may not be working, it helps understand how IP addresses work.

Internet Protocol works the same way as any other language, by communicating using set guidelines to pass information. All devices find, send, and exchange information with other connected devices using this protocol. By speaking the same language, any computer in any location can talk to one another.

The use of IP addresses typically happens behind the scenes. The process works like this:

1) Your device indirectly connects to the internet by connecting at first to a network connected to the internet, which then grants your device access to the internet. When you are at home, that network will probably be your Internet Service Provider (ISP). At work, it will be your company network.

2) Your IP address is assigned to your device by your ISP since they are giving you access to the internet. Your internet activity goes through the ISP, and they route it back to you, using your IP address. 

3) However, your IP address can change. For example, turning your modem or router on or off can change it. Or you can contact your ISP, and they can change it for you.

4) When you are out and about and you take your device with you, your home IP address does not come with you. This is because you will be using another network (Wi-Fi at a hotel, airport, or coffee shop, etc.) to access the internet and will be using a different (and temporary) IP address, assigned to you by the ISP of the hotel, airport or coffee shop.


## Key-terms
[Public IP Addresses](https://github.com/techgrounds/cloud-6-repo-NederLANA/blob/main/beschrijvingen/general-glossary.md#private-ip-addresses)

[Private IP Addresses](https://github.com/techgrounds/cloud-6-repo-NederLANA/blob/main/beschrijvingen/general-glossary.md#public-ip-addresses)

[NAT IP](https://github.com/techgrounds/cloud-6-repo-NederLANA/blob/main/beschrijvingen/general-glossary.md#nat-ip)

[IPv4 vs IPv6 Addresses](https://github.com/techgrounds/cloud-6-repo-NederLANA/blob/main/beschrijvingen/general-glossary.md#ipv4-vs-ipv6-addresses)

## Assignment
1) Find out what your public IP address is of your laptop and mobile on WiFi
2) Find out what your public IP address is on your mobile via mobile internet (if possible)
3) Create a VM in your cloud with a public IP. Connect to this VM.
4) Remove the public IP address from your VM. Understand what is happening with your connection.

*Don't forget to delete the VMs and extra resources (clean up) when done.*

### References
https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address

https://whatismyipaddress.com/nat

https://www.manageengine.com/network-configuration-manager/configlets/what-is-nat.html

https://www.juniper.net/us/en/research-topics/what-is-ipv4-vs-ipv6.html

finding laptop public/private ip:
https://www.businessinsider.com/how-to-find-ip-address-on-windows?international=true&r=US&IR=T

https://www.whatismyip.com/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses


### Issues
None

### Results

1) By testing public IP address from the following website: www.whatismyip.com, both laptop and mobile devices have the same public IP assigned by Ziggo ISP (as expected)

![image](https://user-images.githubusercontent.com/4924632/146779117-a59d9ef6-6647-4b09-be25-144c4fd08156.png)

2) By turning off the wifi signal, and reverting to 4G, the mobile device is now connecting to Vodafone for internet connection, and therefore different public IP is assigned by diff ISP (as expected)

<image src="https://user-images.githubusercontent.com/4924632/146780135-975759e0-ce10-48f6-86eb-2af6f571f11c.png" width="300">
  
3) Create an AWS EC2 instance with a public IP address and connect to the ec2. (Enabled public IPv4 assigned in subnet upon launch of instance).
  
<image src="https://user-images.githubusercontent.com/4924632/146837735-34ded050-917a-4cec-a666-084495bd0b57.png" width="400">
  
In the AWS documentation:
>You cannot manually associate or disassociate a public IP (IPv4) address from your instance. However: 

>-We release your instance's public IP address when it is stopped, hibernated, or terminated. Your stopped or hibernated instance receives a new public IP address when it is started.
-If the public IP address of your instance in a VPC has been released, it will not receive a new one if there is more than one network interface attached to your instance.
-If your instance's public IP address is released while it has a secondary private IP address that is associated with an Elastic IP address, the instance does not receive a new public IP address.
  
4) Remove public IP address from ec2 (in this instance, AWS releases the instance public IP address when it is stopped.)
  
![image](https://user-images.githubusercontent.com/4924632/146838147-6f14702e-9093-46f1-b3f3-996c2ba0e66d.png)
![image](https://user-images.githubusercontent.com/4924632/146838206-6522bb2f-e7be-4996-ae77-554b7468b153.png)

  
  
  



