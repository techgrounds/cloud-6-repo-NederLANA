# AWS Global Infrastructure

In the cloud, everything from servers to networking is virtualized. As an AWS customer, you don’t have to worry about the underlying physical infrastructure. That being said, the physical location of an application in the cloud can be important.AWS has a global infrastructure made up of the following components:
Regions
Availability Zones
Edge Locations

As a customer, you have different amounts of control over where your stuff is located depending on the service you use.For example, IAM is a global service, so you get no control over where its information is stored. In contrast, you can select specific Availability Zones for RDS instances.

## Key-terms
* AWS Global Infrastructure
* Regions
* Availability Zones (AZ)
* Edge Locations (Amazon CloudFront)

## Opdracht
### Wat is een AWS-beschikbaarheidszone?
High availabilty and fault tolerance
Regions are not one location (to be disaster proof). Each regionis made up of multiple data centers. 

A single data center (dc) or a group of dc is called an Availability Zone (AZ). Each AZ is 1+ dc with redundant pwoer, networking, and connectivity. Best practice is to run across at least 2 AZ in 1 region. 

Many AWS services run at the Region level, meaning synchronously across multiple AZ automatically with no additional cost or effort from customer.

**Any service listed as regional is=high availibility.**

### Wat is een regio?
AWS has set up a global infrastructure, linking large groups of data centers across the world called "Regions" 

AWS builds Regions to be closest to where the business traffic demands. Locations like Paris, Tokyo, Sao Paulo, Dublin, Ohio. Inside each Region, we have multiple data centers that have all the compute, storage, and other services you need to run your applications. Each Region can be connected to each other Region through a high speed fiber network, controlled by AWS

The business decision maker, gets to choose which Region you want to operate from. Each Region is isolated from every other Region in the sense that absolutely no data goes in or out of your environment in that Region without you explicitly granting permission for that data to be moved. This is a critical security feature (ex: gov compliance requirements regarding data movements). This is called *regional data sovereignty*, with data being subject to the local laws of the country where the Region lives. 
4 factors to consider when choosing region:
1) Compliance-are you limited by local laws?
2) Proximity-closer reduces latency.
3) Feature availability-complex features are built out one region at a time, like quantum computing platform.
4) Pricing-if budget is the main concern, go with the cheapest region.

### Wat is een Edge-locatie?
An edge location is a site that Amazon CloudFront uses to store cached copies of your content closer to your customers for faster delivery.

Caching copies of data closer to the customers all around the world uses the concept of content delivery networks, or CDNs aka CloudFront. CloudFront uses Edge locations, to reduce latency. Edge locations are separate from Regions, so you can push content from inside a Region to a collection of Edge locations around the world. 

Edge locations also run a domain name service (DNS) aka Route 53, to further help direct customers to the correct web locations. 

![image](https://user-images.githubusercontent.com/4924632/145838092-aa4838db-ba24-4662-b1a7-815131159482.png)

### Waarom zou je de ene regio verkiezen boven de andere? (bijv. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).
4 reasons:
1) Compliance-You may have a business US or Oregon based business that legally requires you to comply to local laws preventing you from moving data outside of that area/country. 
2) Proximity-You may have a business where most of your users are from Oregon or much nearer to that region than to Frankfurt.
3) Feature availibilty-Amazon has a feature that you need, but is currently available in the Oregon region, and not Frankfurt. 
4) Pricing-Your business is pricing sensitive, that any higher latency is worth saving the money of a lower pricing model that the Oregon region may offer. 


### Gebruikte bronnen
https://explore.skillbuilder.aws/learn/course/134/play/31418/aws-cloud-practitioner-essentials-all-modules


### Ervaren problemen
The assignment was given in English and the answers were also found in English, so I after some translating back and forth, it is simplest to keep it all in English for continuity instead of a hodge podge of both languages. Some key terms are nuanced and should remain in original language to prevent obsfucation.

### Resultaat

