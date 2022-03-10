from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    NestedStack,
    aws_cloudformation as cfn,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_kms as kms,
    aws_iam as iam,
)

class Ec2Ns(cfn.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

 amzn_linux = ec2.MachineImage.latest_amazon_linux(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                                 edition=ec2.AmazonLinuxEdition.STANDARD,
                                 virtualization=ec2.AmazonLinuxVirt.HVM,
                                 storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
                                    )

         #Role
        role1= iam.Role(self,"role1",
                              assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                           )
        role1.add_managed_policy(
                                 iam.ManagedPolicy.from_aws_managed_policy_name
                                 ("AmazonSSMFullAccess")
                                 )
        #Key Pair
        key = KeyPair(self,"KeyPair",
                        name="WebServerKey",
                        store_public_key=True
                     )

        key.grant_read_on_private_key(role1)
        key.grant_read_on_public_key(role1)
        with open("./userdata.sh") as f:
                    user_data = f.read()