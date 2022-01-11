# DynamoDB
Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale, that would overburden traditional relational databases.. DynamoDB offers built-in security, continuous backups, automated multi-region replication, in-memory caching, and data export tools. 

![](../00_includes/wk04/dynamoDB-flowchart.png)

DynamoDB features:
* Global tables - 
* Point-in-time recovery - 
* NoSQL Workbench - 
* DynamoDB Accelerator (DAX) - 

Relational database systems (RDBMS) and NoSQL databases have different strengths and weaknesses:

In RDBMS, data can be queried flexibly, but queries are relatively expensive and don't scale well in high-traffic situations (see First Steps for Modeling Relational Data in DynamoDB).

In a NoSQL database such as DynamoDB, data can be queried efficiently in a limited number of ways, outside of which queries can be expensive and slow.

These differences make database design different between the two systems:

* In RDBMS, you design for flexibility without worrying about implementation details or performance. Query optimization generally doesn't affect schema design, but normalization is important.

* In DynamoDB, you design your schema specifically to make the most common and important queries as fast and as inexpensive as possible. Your data structures are tailored to the specific requirements of your business use cases.

**Approaching NoSQL Design**

The first step in designing your DynamoDB application is to identify the specific query patterns that the system must satisfy.

In particular, it is important to understand three fundamental properties of your application's access patterns before you begin:

1) Data size: Knowing how much data will be stored and requested at one time will help determine the most effective way to partition the data.

2) Data shape: Instead of reshaping data when a query is processed (as an RDBMS system does), a NoSQL database organizes data so that its shape in the database corresponds with what will be queried. This is a key factor in increasing speed and scalability.

3) Data velocity: DynamoDB scales by increasing the number of physical partitions that are available to process queries, and by efficiently distributing data across those partitions. Knowing in advance what the peak query loads will be might help determine how to partition data to best use I/O capacity.

After you identify specific query requirements, you can organize data according to general principles that govern performance:

1) Keep related data together.   Research on routing-table optimization 20 years ago found that "locality of reference" was the single most important factor in speeding up response time: keeping related data together in one place. This is equally true in NoSQL systems today, where keeping related data in close proximity has a major impact on cost and performance. Instead of distributing related data items across multiple tables, you should keep related items in your NoSQL system as close together as possible.

2) As a general rule, you should maintain as few tables as possible in a DynamoDB application.
Exceptions are cases where high-volume time series data are involved, or datasets that have very different access patterns. 

3) Use sort order.   Related items can be grouped together and queried efficiently if their key design causes them to sort together. This is an important NoSQL design strategy.

4) Distribute queries.   It is also important that a high volume of queries not be focused on one part of the database, where they can exceed I/O capacity. Instead, you should design data keys to distribute traffic evenly across partitions as much as possible, avoiding "hot spots."

5) Use global secondary indexes.   By creating specific global secondary indexes, you can enable different queries than your main table can support, and that are still fast and relatively inexpensive.

These general principles translate into some common design patterns that you can use to model data efficiently in DynamoDB.


## Key-terms
[NoSQL]()

## Assignment


### References
https://aws.amazon.com/dynamodb/

labs:
https://aws.amazon.com/dynamodb/getting-started/?pg=dynamodbt&sec=hs

https://amazon-dynamodb-labs.com/hands-on-labs.html

### Issues


### Results
