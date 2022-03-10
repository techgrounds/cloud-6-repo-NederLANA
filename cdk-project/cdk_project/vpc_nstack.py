from constructs import Construct
from aws_cdk import (
    Duration,
    NestedStack,
    Stack,
    aws_cloudformation as cfn,
    aws_ec2 as ec2,
)


class VpcNstack(cfn.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
            self, "app-vpc",
            cidr="10.10.10.0/24",
            # for now, just configuring 1 public subnet in in each of 2 AZ
            max_azs=2,
            nat_gateways=0, #uncomment if private subnet required with internet access
            subnet_configuration=[
                ec2._SubnetConfiguration(name="public", cidr_mask=26, subnet_type=ec2.SubnetType.Public),
                # ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE),
                ]
            )