from aws_cdk import (
    aws_cloudformation as cfn,
    aws_ec2 as ec2,
    core
)

class AppStack (cfn.NestedStack):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        vpc: ec2.Vpc,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        ec2.Instance(
            self,
            f'{id}Ec2Instance',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.generic_linux(
                ami_map={
                    'us-west-2': 'ami-04590e7389a6e577c'
                }
            ),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_name='public')
        )