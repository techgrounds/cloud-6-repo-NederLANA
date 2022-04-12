"""
ecs patterns
launches application load balanced fargate


"""

from tkinter import N
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    CfnOutput,
    NestedStack,
    Duration,
    Stack,
    RemovalPolicy,
    Tags,
    aws_backup as backup,
    aws_events as events,
    aws_iam as iam,
    aws_ssm as ssm
)
from aws_cdk.aws_certificatemanager import Certificate
from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
from constructs import Construct
from cdk_ec2_key_pair import KeyPair


class EcsPatterns(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #VPC1 for web server in 2 AZ
        self.vpc1=ec2.Vpc(self, vpc1, max_azs=2, cidr="10.10.10.0/24")
        CfnOutput(self, "Output1", value=self.vpc1.vpc_id)
        cluster=ecs.Cluster(self, "MyCluster", vpc=self.vpc1)

        certificate=Certificate.from_certificate_arn(self, "Cert", "arn:aws:acm:eu-central-1:933140668725:certificate/e1b2c88d-7ec4-4e0e-bed4-3a5925d811e7")

        ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "MyFargateService",
            cluster=cluster, # Required to call from vpc1
            certificate=certificate,
            ssl_policy=SslPolicy.RECOMMENDED,
            redirect_http=True,
            cpu=512,                    # Default is 256
            desired_count=2,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")),
            memory_limit_mib=2048,
            public_load_balancer=True,
        )