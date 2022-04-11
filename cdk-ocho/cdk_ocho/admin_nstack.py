from aws_cdk import (
    NestedStack,
    CfnOutput,
    aws_ec2 as ec2,
)
from constructs import Construct

class AdminNstack(NestedStack):

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

        #AMI Linux for web server
        amzn_linux=ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        #AMI Windows for admin server to connect to web servia via SSH and/or RDP
        windows_server=ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE
        )

        #SG for Admin Server allows all outbound traffic
        AdminSG=ec2.SecurityGroup(
            self,"AdminSG",
            vpc=self.vpc2,
            allow_all_outbound=True,
            security_group_name="AdminServerSG")

        #SG allows SSH ingress to Admin Server from trusted IP
        AdminSG.add_ingress_rule(
            ec2.Peer.ipv4("83.80.144.156/32"), #insert user IP
            ec2.Port.tcp(22),
            "SSH to admin server from trusted ip"
        )

        #SG allows RDP ingress to Admin Server from trusted IP
        AdminSG.add_ingress_rule(
            ec2.Peer.ipv4("83.80.144.156/32"),
            ec2.Port.tcp(3389),
            "RDP to admin server from trusted ip"
        )

        #SG allows only secured access to Admin Server.
        AdminSG.add_ingress_rule(
            ec2.Peer.ipv4("83.80.144.156/32"),
            ec2.Port.tcp(443),
            "HTTPS secured access to admin server from trusted ip"
        )

        #NOT RECOMMENDED: SG allowing unsecured access to Admin Server with public IP
        AdminSG.add_ingress_rule(
            ec2.Peer.ipv4("83.80.144.156/32"),
            ec2.Port.tcp(80),
            "unsecured HTTP access to Admin Server from trusted IP")