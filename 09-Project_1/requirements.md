
## App construct tree:

├── App
│   ├── Stack 1
│   │   ├── VPC Admin Server[L1 Construct](... properties ...)
|   |   |   |__ Public subnets (ACL)
|   │   │   |__ IAM Role (policy information)
|   │   │   |__ Asset Code (Handler, pointer to S3 location where Asset will reside)
|   │   │   |__ Lambda Function (Function definition and properties)
|   |   |   |__ EC2 launch (AMI, SG, VPC peering/bastion host, IAM/AD, or Secret Manager)
|   |   |   |
|   |   |__ VPC Web Server[L1 Construct](... properties ...)
|   |   |   |__ Public subnets (ACL)
|   │   │   |__ IAM Role (policy information)
|   │   │   |__ Asset Code (Handler, pointer to S3 location where Asset will reside)
|   |   |   |__ EC2 launch (auto scaling, LB, SG, AMI, encrypted storage KMS, user data)
|   |   |
|   |__ Stack 2
|   |   |__ Backup Service (S3, Server Manager, cron job)
|   |   |__ Monitoring (Cloudwatch, SQS)
|   |   |__ Test
|   |   |
|   |__ Stack 4* optional?
|   |   |__ CI/CD (post-deployment/bootstrap script, S3)
|   |   |__ Github Events

