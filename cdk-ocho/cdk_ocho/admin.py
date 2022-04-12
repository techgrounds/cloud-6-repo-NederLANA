from aws_cdk import (
    NestedStack,
    CfnOutput,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
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
from constructs import Construct
from cdk_ec2_key_pair import KeyPair

class Admin(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #VPC2 administrator server
        self.vpc2=ec2.Vpc(self, "AdminVpc", max_azs=2,
            cidr="10.20.20.0/24", subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public"
                )
            ]
        )
        CfnOutput(self, "Output2",value=self.vpc2.vpc_id)


        #AMI Windows for admin server to connect to web servia via SSH and/or RDP
        windows_server=ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE
        )


        #Key Pair Admin Server
        admin_key=KeyPair(
            self,"KeyPair2",
            name="AdminServerKey",
            store_public_key=True
        )


        #SG for Admin Server allows all outbound traffic
        AdminSG=ec2.SecurityGroup(
            self,"AdminSG",
            vpc=self.vpc2,
            allow_all_outbound=True,
            security_group_name="AdminServerSG")


        #EC2(2) for Admin Server in VPC2
        instance2=ec2.Instance(
            self, "InstanceAdmin",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=windows_server,
            vpc=self.vpc2,
            security_group=AdminSG,
            key_name=admin_key.key_pair_name,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        volume_type=ec2.EbsDeviceVolumeType.GP2,
                        encrypted=True
                    ),
                    mapping_enabled= True
                )
            ]
        )
        Tags.of(instance2).add(key="admins",value="AdminBackup")
