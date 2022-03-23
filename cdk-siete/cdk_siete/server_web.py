from aws_cdk import (
    # Duration,
    #Stack,
    NestedStack,
    #RemovalPolicy,
    CfnOutput,
    #Tags,
    aws_ec2 as ec2,
    #aws_ssm as ssm,
    #aws_backup as backup,
    #aws_events as events,
    #aws_iam as iam
)
from constructs import Construct

class ServerWeb(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
#web server vpc
        self.vpcweb = ec2.Vpc(
                    self, "vpcweb",
                    cidr="10.10.10.0/24",
                    # for now, just configure 1 public subnet in each of the 2 AZ
                    max_azs=2,
                    nat_gateways=0, #uncomment if private subnet is created and requires internet access
                    subnet_configuration=[
                        ec2.SubnetConfiguration(name="public-web", subnet_type=ec2.SubnetType.PUBLIC),
                        # ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE),
                        ]
                    )

        CfnOutput(self, "Outputweb",
                       value=self.vpcweb.vpc_id)