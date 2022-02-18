# Networking Devices
Introduction:
There is no network without networking equipment if you want to connect more than two computers together. 

Each device helps ensure that data is delivered to the right computer. Often they function together so that the user doesn't have to worry about settings. Network devices keep working even when new computers or devices are added or removed to the network. This is where protocols are important. 

AWS and Azure offer services that are similar to what network devices do. And every networking concept (routing, switching, gateways) has one or more cloud equivalents.


## Key-terms
For understanding how the different network devices work, these two aspects of the OSI model will help:

[The layer](https://github.com/techgrounds/cloud-6-repo-NederLANA/blob/main/beschrijvingen/general-glossary.md#the-layer)

[Protocol data unit (PDU)](https://github.com/techgrounds/cloud-6-repo-NederLANA/blob/main/beschrijvingen/general-glossary.md#protocol-data-unit-pdu)

## Assignment
Study:
Network Devices
The OSI model in relation to these network devices.

Assignment:
Name and describe the functions of common network devices
Most routers have a list of all connected devices, find this list. What other information does the router have about connected devices?
The default settings
Where is your DHCP server located on your network? What are its configurations?

### References
https://www.auvik.com/franklyit/blog/network-devices/

https://www.educba.com/types-of-network-devices/

### Issues


### Results

**11 types of network devices**

**1. Firewall**
A firewall is a network security device that monitors and either blocks or allows traffic based on a set of rules. Firewalls can be software, hardware, or a combination of both. Additionally, the rules firewalls use can be based on something straightforward like ports and IP addresses or use heuristics to identify malicious behavior.

Common examples of network firewalls include:

Packet-filtering firewalls: These firewalls operate at Layer 3 and Layer 4 and determine whether to drop or forward traffic using rules based on basic information like IP addresses, port numbers, and packet type. One of the upsides of this simple approach to inspecting traffic is that it has little impact on network speed.

Stateful-inspection firewalls: Unlike packet-filtering firewalls, stateful-inspection firewalls can track and “understand” when a TCP connection has occurred. This allows for reply traffic to be allowed through the firewall without the need for explicit rules. As a result, stateful-inspection firewalls make configuration easier, but can add a bit more inspection overhead and slow down traffic slightly more than packet-filtering firewalls.

Application firewalls: These firewalls operate at Layer 7 and can contextualize what’s normal vs malicious behavior for application-layer protocols like HTTPS, SSH, and SMTP. Proxy firewalls that provide URL filtering and WAFs (web application firewalls) that protect against cross-site scripting (XSS) and SQL injection attacks are two common types of application firewalls.

Next-generation firewalls (NGFWs) and unified threat management (UTM) appliances: In general, these two popular types of firewalls share many of the same features. In addition to providing the functionality of the other types of firewalls mentioned, these more advanced network security devices add advanced features like deep packet inspection (DPI), heuristics that can detect malware, and inspection of encrypted traffic to the mix.

**2. Switch**
The textbook definition of a network switch is a Layer 2 device that sends and receives frames. These switches are the basic building block of Ethernet networks. You can see a switch as a system that combines some of the best routers and hubs.

Here’s a basic example of how a Layer 2 switch works:

Devices are connected to the switch using Ethernet cables (e.g., a Cat5e or Cat6 cable) creating a small LAN.
The switch learns the MAC addresses of the connected devices.
When traffic needs to go to a specific device, the switch sees the MAC address in the packet and sends it to only that device.
By sending the data to a specific device, the switch is breaking up collision domains and greatly reducing network congestion when compared to network hubs. That breaking up of collision domains is the basic benefit of a Layer 2 switch.

However, this basic example of a Layer 2 switch is just one of the many types of network switches. Here’s a list of common types of network switches:

Unmanaged switches: Unmanaged switches simply provide Layer 2 switching of Ethernet frames. They don’t offer any additional management or configuration features.
PoE switches: Switches that provide Power over Ethernet (PoE) functionality can provide both network connectivity and power to connected devices. For example, it’s common to power Voice over IP (VoIP) phones using PoE switches. PoE switches can be Layer 2 or Layer 3 switches and can be managed or unmanaged.

Managed switches: Managed switches vary greatly in their features and functionality. For example, some managed switches are targeted to gamers for use at home while others are targeted to large enterprises for use on corporate networks. One of the most important aspects of a managed switch is the ability to create VLANs (virtual LANs). Other popular managed switch features include QoS (quality of service) to prioritize certain types of traffic and Spanning Tree Protocol (STP) to prevent network loops. Managed switches can be either Layer 2 or Layer 3 switches.

Layer 3 switches: These switches offer the same Layer 2 functionality as other switches, but add Layer 3 routing to the mix. Layer 3 switches are aware of IP addresses and can route packets between networks.

Stackable switches: Some network switches can be “stacked”. These stackable switches can be connected to one another to operate as a single logical switch. Stacking switches can be a useful way to increase the capacity of a network. For example, stacking two 24-port switches would create a single 48-port switch from a management and functionality perspective.

**3. Access point**
Operating at Layer 2, access points (APs)—also known as wireless access points (WAPs)—are the network switches of the wireless world. WAPs connect to a LAN through a wired connection and allow other Wi-Fi devices to communicate. The networks created by WAPs are WLANs (wireless local area networks).

At a high level, there are three main types of APs:

Fat APs: Fat access points are also known as autonomous APs. Fat APs directly handle the forwarding of traffic from their Wi-Fi radios to the wired network. These WAPs have interfaces where you can access and configure things like access control lists, Wi-Fi encryption, DHCP server functionality, and QoS directly. The upside of fat APs is that they’re an all-in-one solution in that they have everything you need to configure and manage the device baked in.

Thin APs: These APs don’t offer the full functionality of an autonomous AP. Instead, they backhaul Wi-Fi traffic to a centralized WLAN controller that handles all the forwarding and functionality a fat AP would do on its own. While the limited functionality of thin APs has some tradeoffs, this centralized approach to WAP management can make large-scale deployments easier to manage.

Fit APs: These WAPs offer a mix of fat and thin AP functionality. For example, most fat APs will handle Wi-Fi encryption at the AP level instead of waiting until the traffic gets back to the controller and may offer services like DHCP relay, but a centralized controller will be used for things like bridging forwarding traffic between wired and wireless networks.

**4. Router**
Routers are the network devices that route packets between networks. These Layer 3 devices enable everything from communication between multiple subnets within the same WAN to the internet connection that show this webpage. Routers are the network device that deals with IP addresses.

**5. NAS (Network attached storage)**
A NAS is a server dedicated to file storage. Within a LAN, a NAS provides a central storage point that can be used for things like shared access to files and storing backups of user data. NAS devices generally provide an affordable and simple way to provide network storage. In recent years, the lines between a NAS device and a general-purpose server are getting even more blurred as NASes begin to offer more advanced functionality suited to small and mid-sized environments.

**6. Load balancer**
Load balancers distribute connections from clients across multiple servers. As with firewalls, there are plenty of software and hardware implementations of load balancers. Load balancers usually operate at Layer 4 (filtering based on TCP or UDP traffic) or Layer 7 (filtering based on HTTP or DNS traffic). Common approaches to load balancing include:

Round-robin: Simply forwards requests to each server in a cycle.

Weighted round-robin: Like round-robin, but takes into account “weights” that help determine what amount of connections a given server should be sent.

Least connections: A form of load balancing that prioritizes sending connections to the server with the fewest connections.

Weighted least connections: Like weighted round-robin, weighted least connections allows the servers to be assigned “weights” that influence the load balancing algorithm.

**7. Repeater**
A repeater is a simple Layer 1 device that rebroadcasts a signal. Repeaters are sometimes referred to as signal boosters. There are repeaters for Wi-Fi, Ethernet, and other network connections, but fundamentally they do the same thing: take a signal in and rebroadcast it.

Pro tip: Simple Wi-Fi repeaters can lead to significant network congestion. If you’re looking to optimize performance, a WAP is often a better choice.

**8. Gateway**
From a hardware perspective, there’s no difference between a gateway and a router. Gateways are simply routers that serve a specific purpose. Gateways are routers that act as the default next hop. When there’s no other route to an IP address on a network, the packets get routed to the network’s default gateway. From there, the default gateway routes the packets on to their next “hop” and the process repeats until the destination is reached.

**9. Modem**
By the traditional definition, a modem is a device that modulates and demodulates a signal to and from analog and digital. In the days of dial-up internet, modems were used to connect local computer networks to analog telephone lines for internet access. Today, when people say “modem” they may be referring to any number of devices that allow connection to a carrier’s network.

Examples of popular types of modems include:

Analog modems
Cable modems
Cellular modems
Fiber optic modems
xDSL modems

**10. Hub**
A hub is a simple type of Ethernet repeater that operates at Layer 1, enabling the connection of multiple devices to the same Ethernet network. Unlike a switch, a hub does NOT break up collision domains, meaning all ports on a network hub get sent the same traffic. As a result, hubs—similar to WiFi repeaters—can cause quite a bit of congestion.

Pro tip: By rebroadcasting traffic to all ports, hubs can create significant network congestion. If you have a use case for a hub, consider an unmanaged switch, which will break up collision domains, instead.

**11. Bridge**
Traditionally, network bridges were Layer two devices that often had only two ports. Like switches, they broke up collision domains and could reduce network congestion when compared to hubs by separating the network into multiple collision domains.

However, today the term “bridge” can mean a lot more than that traditional definition depending on the context. Other interpretations of the term network bridge:

A device that can connect VLANs at Layer 2
A network switch
A device that can connect two networks using different connection mediums, such as connecting a WLAN to a wired LAN

**What about “brouters”?**
As the name implies, these hybrid devices deliver the Layer 2 bridging functionality of a bridge and the Layer 3 routing functionality of a router.

---


