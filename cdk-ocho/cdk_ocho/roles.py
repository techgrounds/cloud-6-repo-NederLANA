from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    CfnOutput,
    NestedStack,
    aws_iam as iam,
    aws_ssm as ssm
)
from constructs import Construct
from cdk_ec2_key_pair import KeyPair
import aws_cdk as cdk

class Roles(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Instance role and SSM Managed policy
        role=iam.Role(
            self, "InstanceSSM",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("SSMManagedInstance")
        )