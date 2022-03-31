from constructs import Construct
from cdk_ec2_key_pair import KeyPair
from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    RemovalPolicy,
    Tags,
    aws_ec2 as ec2,
    aws_backup as backup,
    aws_events as events
    #aws_iam as iam,
    #aws_ssm as ssm,
)

class CdkSeisStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #VPC1: web server
        self.vpc1=ec2.Vpc(
            self, "VPC",
            max_azs=2,
            cidr="10.10.10.0/24",
            subnet_configuration=[
               ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=26
               )
            ]
        )

        CfnOutput(
            self, "Output1",
            value=self.vpc1.vpc_id)

        #VPC2 administrator server
        self.vpc2=ec2.Vpc(
            self, "VPC2",
            max_azs=2,
            cidr="10.20.20.0/24",
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=26
                )
            ]
        )

        CfnOutput(
            self, "Output2",
            value=self.vpc2.vpc_id)

        # Peering between VPC1 and VPC2
        self.VPC1PeerVPC2=ec2.CfnVPCPeeringConnection(
            self,
            "VPC1PeerVPC2",
            peer_vpc_id=self.vpc1.vpc_id,
            vpc_id=self.vpc2.vpc_id,
            peer_region="eu-central-1"
        )

        for i in range(0,1):
            self.cfn_Route=ec2.CfnRoute(self, "VPC1RouteVPC2",
            route_table_id=self.vpc.public_subnets[i].route_table.route_table_id,
            destination_cidr_block="10.20.20.0/24",
            vpc_peering_connection_id=self.VPCPeering.ref)

        for i in range(0,1):
            self.cfn_Route=ec2.CfnRoute(self, "VPC2RouteVPC1",
            route_table_id=self.vpc2.public_subnets[j].route_table.route_table_id,
            destination_cidr_block="10.10.10.0/24",
            vpc_peering_connection_id=self.VPCPeering.ref)


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
            vpc= self.vpc2,
            allow_all_outbound=True,
            sg_name="AdminServerSG"
        )

        #SG allows SSH ingress to Admin Server from trusted IP
        AdminSG.add_ingress_rule(
            trusted_ip=ec2.Peer.ipv4("83.80.144.156/32"), #insert user IP
            connect_port=ec2.Port.tcp(22),
            ingress_name="SSH"
        )

        #SG allows RDP ingress to Admin Server from trusted IP
        AdminSG.add_ingress_rule(
            trusted_ip=ec2.Peer.ipv4("83.80.144.156/32"),
            connect_port=ec2.Port.tcp(3389),
            ingress_name="RDP"
        )

        #SG allows only secured access to Admin Server
        AdminSG.add_ingress_rule(
            trusted_ip=ec2.Peer.ipv4("83.80.144.156/32"),
            connected_port=ec2.Port.tcp(443),
            ingress_name="HTTPS"
        )

        #NOT RECOMMENDED: SG allowing unsecured access to Admin Server with public IP
        AdminSG.add_ingress_rule(
            trusted_ip=ec2.Peer.ipv4("83.80.144.156/32"),
            connected_port=ec2.Port.tcp(80),
            ingress_name="HTTP")

        #Security Group for web server
        WebSG=ec2.SecurityGroup(
            self,"WebSG",
            vpc= self.vpc1,
            allow_all_outbound=True,
            sg_name="WebserverSG"
        )

        #SG allows unsecured internet traffic public IP
        WebSG.add_ingress_rule(
            unsecured_public=ec2.Peer.any_ipv4(),
            connect_port=ec2.Port.tcp(80),
            ingress_name="HTTP public traffic"
        )

        #SG allows secured public internet traffic
        WebSG.add_ingress_rule(
            secured_public=ec2.Peer.any_ipv4(),
            connect_port=ec2.Port.tcp(443),
            ingress_name="HTTPS public traffic"
        )

        #SG allows private RDP ingress from Admin Server
        WebSG.add_ingress_rule(
            admin_id=ec2.Peer.ipv4(AdminSG.security_group_id),
            connect_port=ec2.Port.tcp(3389),
            ingress_name="RDP from Admin Server"
        )
        #SG allows private SSH ingress from Admin Server
        WebSG.add_ingress_rule(
            admin_id=ec2.Peer.security_group_id(AdminSG.security_group_id) ,
            connect_port=ec2.Port.tcp(22),
            ingress_name="SSH from Admin Server"
        )

        #Key Pair Web Server
        key = KeyPair(
            self,"KeyPair1",
            name="WebServerKey",
            store_public_key=True
        )

        #EC2 Admin Server
        instance2=ec2.Instance(
            self, "Instance2",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=amzn_linux,
            vpc=self.vpc2,
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
            ],
            security_group = MgmtSG,
            key_name=key1.key_pair_name
        )



        #Web server EC2 launch
        instance1 = ec2.Instance(self, "Instance",
        instance_type=ec2.InstanceType("t2.micro"),
        machine_image=amzn_linux,
        vpc = self.vpc,
        block_devices= [ec2.BlockDevice(
                        device_name="/dev/xvda",
                        volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        volume_type=ec2.EbsDeviceVolumeType.GP2,
                        encrypted=True
                         ),
                         mapping_enabled= True
                         )
                         ],
        user_data=ec2.UserData.custom(user_data),
        security_group = webSG,
        key_name=key.key_pair_name
        )
        instance1.connections.allow_from_any_ipv4(port_range=ec2.Port.tcp(80)
                                                  , description="Allow Web Traffic")

        CfnOutput(self,"ip", value=str(instance1.instance_private_ip))




        #Key Pair Admin Server
        key1 = KeyPair(
            self,"KeyPair2",
            name="AdminServerKey",
            store_public_key=True
        )

        #Network ACL
        aclcidr1= ec2.AclCidr.any_ipv4()
        nacl=ec2.NetworkAcl(self,"mynacl",vpc=self.vpc2)
        nacl.add_entry("id",cidr=aclcidr1,rule_number=100,
               traffic=ec2.AclTraffic.all_traffic(),direction=ec2.TrafficDirection.EGRESS,
                  network_acl_entry_name="myentry",rule_action=ec2.Action.ALLOW)



        #server Tags
        Tags.of(instance1).add(key="webs",value="webbackup")
        Tags.of(instance2).add(key="mgmt",value="mgmtbackup")

        #Back up Web Server
        wsvault= backup.BackupVault(self,"wsvault",backup_vault_name="wsvault",removal_policy=RemovalPolicy.DESTROY)
        backup_plan1 = backup.BackupPlan(self,"Backup1",backup_plan_name="wsbackup")
        backup_plan1.add_selection("ebsResource",resources=[backup.BackupResource.from_tag(key="webs",value="webbackup")]
                                                            )

        backup_plan1.add_rule(backup.BackupPlanRule(
                              backup_vault=wsvault,
                              rule_name="WebRule",
                              schedule_expression=events.Schedule.cron(hour="4" ,minute="00",day="*", month="*",year="*"),
                              delete_after=Duration.days(7),
                              completion_window=Duration.hours(2),
                              start_window=Duration.hours(1)
                               ))

        #Back up Mgmt Server
        mgmtvault= backup.BackupVault(self,"mgmtvault",backup_vault_name="mgmtvault",removal_policy=RemovalPolicy.DESTROY)
        backup_plan2 = backup.BackupPlan(self,"Backup2",backup_plan_name="Mgmtsbackup")
        backup_plan2.add_selection("ebsResource1",resources=[backup.BackupResource.from_tag(key="mgmt",value="mgmtbackup")]
                                                            )

        backup_plan2.add_rule(backup.BackupPlanRule(
                              backup_vault=mgmtvault,
                              rule_name="MgmtRule",
                              schedule_expression=events.Schedule.cron(hour="5" ,minute="00",day="*", month="*",year="*"),
                              delete_after=Duration.days(7),
                              completion_window=Duration.hours(2),
                              start_window=Duration.hours(1)
                               ))