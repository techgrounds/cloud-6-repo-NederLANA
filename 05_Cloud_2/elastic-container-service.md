# Elastic Container Service ECS

Amazon ECS makes it easy to deploy, manage, and scale Docker containerized (long-running)applications, services, batch processes, ETL workloads, microservices, and machine learning apps. Amazon ECS places containers across clusters based on resource needs and is integrated with familiar features like Elastic Load Balancing, EC2 security groups, EBS volumes and IAM roles. 

Companies initially build and deploy their applications in a monolithic design, but as they grow and offer more features, ECS allows them to migrate towards a microservices model and more sophisticated application architecture. 

1) Containers are defined in a task definition that is used to run **tasks** within a service. In this context, a **service** is a configuration that runs and maintains a specified number of tasks simultaneously in a **cluster**. 
* Web servers
* App servers
* Queues
* Background workers
* Caches
* API Backends
* Databases

*Tasks and services can be run on a serverless infrastructure that is managed by AWS Fargate.*

*Alternatively, for more control over the infrastructure, run tasks and services on a cluster of Amazon EC2 instances that is self-managed.*

2) Amazon ECS enables launch and stop of container-based applications by using **simple API calls**. 
*Can also retrieve the state of a cluster from a centralized service and have access to many familiar Amazon EC2 features.*
*Or can configure it through self management.


What is ECS for?
How does X fit / replace X in a classical setting?
How can X be combined with other services?
What is the difference between X and other similar services? Compare to EC2, Kubernetes/EKS

*No additional charge to use ECS to manage containers. Only pay for EC2 or Fargate consumption


## Key-terms
[Container](beschrijvingen/general-glossary.md#container)

[Docker](beschrijvingen/general-glossary.md#docker)

[Kubernetes](beschrijvingen/general-glossary.md#kubernetes)

[Cluster]()

[Monolith]()

[Microservice]()

[Extract-Transform-Load Workloads]()


## Assignment
How is this service linked to other resources/services?


Access ECS from the AWS SDK or AWS management console: https://aws.amazon.com/ecs/

Steps to start ECS:
Deploying a Docker Container to ECS

1) Create the Docker image.
2) Create an ECR registry.
3) Tag the image.
4) Give the Docker CLI permission to access Amazon account.
5) Upload docker image to ECR.
6) Create a Fargate Cluster for ECS to use for the deployment of your container.
7) Create an ECS Task.
8) Run the ECS Task.

### References
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html

https://towardsdatascience.com/deploying-a-docker-container-with-ecs-and-fargate-7b0cbc9cd608

Amazon ECS: Core concepts
https://www.youtube.com/watch?v=eq4wL2MiNqo

EC2 vs ECS vs Lambda
https://www.youtube.com/watch?v=-L6g9J9_zB8

Overview of containers on AWS;
https://www.youtube.com/watch?v=AYAh6YDXuho

Moving from Monolith to Microservices
https://www.youtube.com/watch?v=_ep_yKuDWkE

https://www.cio.com/article/247005/what-are-containers-and-why-do-you-need-them.html
### Issues


### Results
