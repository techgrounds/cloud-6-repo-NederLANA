from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    NestedStack
     CfnOutput,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_kms as kms,
    aws_backup as backup,
    aws_events as events,
    aws_iam as iam,
)

class AdminServer(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

instance2 = ec2.Instance(self, mgmt_instance_id,
                    instance_type=ec2.InstanceType(mgmt_instance_type),
                    machine_image=amzn_linux,
                    vpc = self.vpc2,
                    block_devices= [ec2.BlockDevice(
                                device_name="/dev/xvda",
                                volume=ec2.BlockDeviceVolume.ebs(
                                 volume_size= mgmt_volume_size,
                                volume_type=ec2.EbsDeviceVolumeType.GP2,
                                encrypted=True
                    ),
                    mapping_enabled= True
                     )],

        role=role1,
        security_group = MgmtSG,
        key_name=key1.key_pair_name
        )