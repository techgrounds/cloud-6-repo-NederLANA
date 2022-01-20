# CloudWatch
![](../00_includes/wk05/cloudwatch.svg) Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), IT managers, and product owners. 

![](../00_includes/wk05/cw-features.png)

Modern applications, like those running on microservices architectures, generate large volumes of data in the form of metrics, logs, and events. Amazon CloudWatch presents a single platform to collect, access, and correlate this data across all AWS resources, helping to break down data silos to gain system-wide visibility and quickly resolve issues.

-provides data and actionable insights to monitor applications, respond to system-wide performance changes, and optimize resource utilization. 

-collects monitoring and operational data in the form of logs, metrics, and events and returns a unified view of operational health

-detects anomalous behavior in environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep applications running smoothly.

-natively integrates with more than 70 AWS services, such as Amazon EC2, Amazon DynamoDB, Amazon S3, Amazon ECS, Amazon EKS, and AWS Lambda.

-use **CloudWatch Events** for serverless to trigger workflows with services like AWS Lambda, Amazon SNS, and AWS CloudFormation.

-Metrics are stored separately in Regions, but CloudWatch cross-Region functionality can be used to aggregate statistics from different Regions. 

*Cloudwatch is a monitoring service that gives visibility into the performance and health of AWS resources and applications, whereas Cloudtrail is a service that logs AWS account activity and API usage for risk auditing, compliance and monitoring.*

![](../00_includes/wk05/cw-how-it-works.png)

Access via [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home?p=clw&cp=bn&ad=c)

## Key-terms
[MTTR](beschrijvingen/general-glossary.md#mttr)

[Namespace]()

## Assignment

Configure Amazon CloudWatch to send a notification when CPU Utilization of an instance is lower than 15%, and send alarm notifications to email through SNS.

### References
https://aws.amazon.com/cloudwatch/

https://cloudcompiled.com/blog/cloudwatch-cloudtrail-difference/

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html

https://aws.amazon.com/cloudwatch/getting-started/

https://www.edureka.co/blog/amazon-cloudwatch-monitoring-tool/

### Issues


### Results

1) Creating a CPU utilization metric
![](../00_includes/wk05/cw-set-alarm.png)

2) Creating an alarm to notify when CPU Utilization metric of the instance is lower than 15%
![](../00_includes/wk05/cw-alarm-enabled.png)

3) Send alarm notification through SNS topic to email.
![](../00_includes/wk05/cw-sns-alert.png)
