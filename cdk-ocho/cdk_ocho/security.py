from aws_cdk import (
    NestedStack,
    CfnOutput,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    CfnOutput,
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
import aws_cdk as cdk

class Security(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


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

        #Security Group for web server
        WebSG=ec2.SecurityGroup(
            self,"WebSG",
            vpc= self.vpc1,
            allow_all_outbound=True,
            security_group_name="WebserverSG"
        )



        #SG allows unsecured internet traffic public IP
        WebSG.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "HTTP public traffic to web server"
        )

        #SG allows secured public internet traffic
        WebSG.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "HTTPS public traffic to web server"
        )

        #SG allows private SSH ingress from Admin Server
        WebSG.add_ingress_rule(
            ec2.Peer.security_group_id(AdminSG.security_group_id) ,
            ec2.Port.tcp(22),
            "SSH from Admin Server"
        )

        #VPC2 Network ACL. Can easily be modified to specs
        aclcidr1= ec2.AclCidr.any_ipv4()
        nacl=ec2.NetworkAcl(
            self,"nacl",
            vpc=self.vpc2
        )
        nacl.add_entry(
            "id",cidr=aclcidr1,rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS,
            network_acl_entry_name="allow all outbound traffic",
            rule_action=ec2.Action.ALLOW
        )
