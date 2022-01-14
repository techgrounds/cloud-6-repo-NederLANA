
Binary

### Bits
It reflects the basic logical process of a transistor: a single unit of information reflecting a zero (no charge) or a one (a completed, charged circuit). **There are eight bits in one byte of information.** Colloquially, bits (and their successively larger relatives, such as kilobits, megabits and gigabits) are used to **measure rates of data transfer.** The abbreviation “Mbps” refers to “megabits,” not “megabytes,” per second.

### Bytes
A byte represents eight bits, and is the most commonly used term relating to the amount of information stored within a computer’s memory. When abbreviated, the “B” is capitalized, so as to set it apart from its smaller relative; “Gb” is short for “gigabit,” and “GB” is short for “gigabyte.”

---

IP Addresses

### Private IP Addresses
Every device that connects to your internet network has a private IP address. This includes computers, smartphones, and tablets but also any Bluetooth-enabled devices like speakers, printers, or smart TVs. With the growing internet of things, the number of private IP addresses you have at home is probably growing. Your router needs a way to identify these items separately, and many items need a way to recognize each other. Therefore, your router generates private IP addresses that are unique identifiers for each device that differentiate them on the network.

### Public IP Addresses
A public IP address is the primary address associated with your whole network. While each connected device has its own IP address, they are also included within the main IP address for your network. As described above, your public IP address is provided to your router by your ISP. Typically, ISPs have a large pool of IP addresses that they distribute to their customers. Your public IP address is the address that all the devices outside your internet network will use to recognize your network.

### NAT IP
Network Address Translation (NAT) is the process where a network device, usually a firewall, assigns a public address to a computer (or group of computers) inside a private network. The main use of NAT is to conserve the number of public IP addresses an organization or company must use, for both economy and security purposes on both sides of the firewall.

<image src="https://user-images.githubusercontent.com/4924632/146751169-3a8c396d-a36f-40da-a6a0-df8b389a928e.png" width="600">

### IPv4 vs IPv6 Addresses
IPv6 (IP version 6) is the most recent generation of the Internet Protocol (IP) defined by the Internet Engineering Task Force (IETF).  Whereas IPv6 is intended to eventually replace IPv4, they are tightly mingled right now—most engineers run them together, but separately in what is called "dual stack". Due to the explosion of internet usage and devices, the move to IPv6 became necessary to create more possible IP addresses and the elimination of using NAT. Some other features such as hexidecimal make it more compatible for mobile devices too.
  
<image src="https://user-images.githubusercontent.com/4924632/146752895-a48ea0db-236c-4920-9b48-b9bafef8af29.png" width="600">

  ---
  
Network Devices
  
### The Layer
The OSI model has seven layers starting at the physical layer (Layer 1) and going up to the application layer (Layer 7). Network hardware is often described by the OSI layer it operates at.
  
### Protocol data unit (PDU)
As data is processed at different layers of the OSI model, headers and footers are stripped away, changing the type of PDU being transmitted. For example, when data transmitted at the network layer (Layer 3) is processed by the transport layer (Layer 4), the IP header is no longer needed. The PDU with the IP header at Layer 3 was a packet. The PDU at Layer 4 without the IP header is a segment. Understanding the different PDUs will help make sense of the terminology associated with different networking devices.

Here’s a visual representation of the OSI model and the PDUs (data) associated with each layer.
![image](https://user-images.githubusercontent.com/4924632/148696269-ab8632e1-6aa4-46af-a68a-8ca1225a1998.png)

---

### Domain Name System (DNS)
- translates human readable domain names to machine readable IP addresses. 
- client queries **recursive DNS** for cached IP information. If there's no cached reference, recursive DNS passes the query to an **authoritative DNS** server, which then translates domain names into IP addresses.

---

Elastic Filing System

### Network File System 
-  NFS is a distributed file system protocol that lets users access files over a network similar to the way they access local storage.

---

DynamoDB

### NoSQL
- nonrelational database specifically optimized for applications that require large data volume, low latency, and flexible data models. This optimization is achieved by relaxing data consistency restrictions of other databases.

Types of NoSQL databases

* Key-value: THis database is highly partitionable and allow unmatched horizontal scaling.

* Document: This database is easier for developers to store and query data by using the same document model format that they use in the application code (ex: JSON). Semistructured nature of document databases evolve easily over time. 

* Graph: Purpose is to work with highly connected datasets. 

* In-memory: Where real-time analytics that require microsecond response timres and can have large traffic spikes. Ex: Gaming leaderboards and add-tech applications.

* Search: Many applications output logs, which search databases can be used as a search engine.

### Partition Key
- used to spread data across partitions for scalability. It’s important to choose an attribute with a wide range of values and that is likely to have evenly distributed access patterns. 

### Sort Key
- to enable easy sorting of data. The sort key allows sort or search among all items sharing the same partition key.

### Encryption at Rest
- protects data where it's stored.

### Encryption in Transit
- protects data as it's moved from one location to another. 