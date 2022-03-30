import os.path
from aws_cdk.aws_s3_assets import Asset
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_iam as iam,
)
from constructs import Construct

dirname= os.path.dirname(__file__)

class CdkSieteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc1 = ec2.Vpc(self, 'APP-PROD-VPC',
             cidr = '10.10.10.0/24',
             max_azs = 2,
             subnet_configuration=[
                 ec2.SubnetConfiguration(
                     name = 'Public-Subnet',
                     subnet_type = ec2.SubnetType.PUBLIC,
                     cidr_mask = 26
                 )
             ])

        self.vpc2 = ec2.Vpc(self, 'Management-PROD-VPC',
             cidr = '10.20.20.0/24',
             max_azs = 2,
             subnet_configuration=[
                 ec2.SubnetConfiguration(
                     name = 'Public-Subnet',
                     subnet_type = ec2.SubnetType.PUBLIC,
                     cidr_mask = 26
                 )
             ])
        self.cfn_VPCPeering_connection = ec2.CfnVPCPeeringConnection(self, "MyCfnVPCPeeringConnection",
        peer_vpc_id = self.vpc1.vpc_id,
        vpc_id = self.vpc2.vpc_id,

             # the properties below are optional
        peer_region='eu-central-1',
        )

        #AMI
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        windows_server = ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE

        )

        #Security group ingress and egress rules
        WebserverSG = ec2.SecurityGroup(self, 'SecurityGroup',
            vpc= self.vpc1,
            allow_all_outbound = True,
            description = ' Techgrounds Project webserver security group'
            )

        WebserverSG.add_ingress_rule(
                peer=ec2.Peer.any_ipv4(),
                connection=ec2.Port.tcp(22),
                description='ssh'
            )

        WebserverSG.add_ingress_rule(
                peer=ec2.Peer.any_ipv4(),
                connection=ec2.Port.tcp(80),
                description='HTTP'
            )

        WebserverSG.add_ingress_rule(
                peer=ec2.Peer.any_ipv4(),
                connection=ec2.Port.tcp(443),
                description='HTTPS'
            )



        MgmtServerSG = ec2.SecurityGroup(self, 'SecurityGroup1',
            vpc= self.vpc2,
            allow_all_outbound = True,
            description = 'ManagementserverSecurityGroup'
            )

        MgmtServerSG.add_ingress_rule(
            peer=ec2.Peer.ipv4('83.85.84.131/32'),
            connection=ec2.Port.tcp(22),
            description='ssh'
        )

        MgmtServerSG.add_ingress_rule(
            peer=ec2.Peer.ipv4('83.85.84.131/32'),
            connection=ec2.Port.tcp(3389),
            description='rdp'
        )

        WebserverSG.add_ingress_rule(
            ec2.Peer.security_group_id(MgmtServerSG.security_group_id),
            ec2.Port.tcp(22),
            'allow ssh access from the Management Security Group'
        )


        # Instance role and SSM Managed policy
        role = iam.Role(self, 'InstanceSSM', assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AmazonSSMManagedInstanceCore'))

        # Instance
        Instance = ec2.Instance(self, 'Webserver',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=amzn_linux,
            vpc = self.vpc1,
            security_group=WebserverSG)

        Instance1 = ec2.Instance(self, 'Management Server',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=windows_server,
            vpc = self.vpc2,
            security_group=MgmtServerSG)

        # Scripts in S3 as Asset
        asset = Asset(self, 'Asset', path=os.path.join(dirname, 'UserData.sh'))
        local_path = Instance1.user_data.add_s3_download_command(
            bucket=asset.bucket,
            bucket_key=asset.s3_object_key
        )

        # Userdata executes scripts from S3
        Instance1.user_data.add_execute_file_command(
            file_path=local_path
        )
        asset.grant_read(Instance1.role)
