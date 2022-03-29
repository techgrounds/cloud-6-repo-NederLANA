from aws_cdk import (
    aws_CloudFormation as cfn,
    aws_ec2 as ec2,
    core,
)


class SkeletonStack(cfn.NestedStack):

    def __init__(
        self,
        scope: core.Construct,
        id: str,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(
            self, 'SkeletonVpc',
            cidr='10.0.0.0/16',
            max_azs=99,  # use all available AZs,
            subnet_configuration=[
                {
                    'cidrMask': 28,
                    'name': 'public',
                    'subnetType': ec2.SubnetType.PUBLIC
                },
                {
                    'cidrMask': 28,
                    'name': 'private',
                    'subnetType': ec2.SubnetType.PRIVATE
                }
            ]
        )
