from constructs import Construct
from cdk_ec2_key_pair import KeyPair
import socket
from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    CfnOutput,
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

        #VPC web server
        self.vpc = ec2.Vpc(self, "VPC",
                           max_azs=2,
                           cidr="10.10.10.0/24",
                            subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public",
                                  )
                            ]
                             )

        CfnOutput(self, "Output",
                       value=self.vpc.vpc_id)

        #VPC management server
        self.vpc2 = ec2.Vpc(self, "VPC2",
                           max_azs=2,
                           cidr="10.20.20.0/24",
                            subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public"
                                  )
                            ]
                            )
        CfnOutput(self, "Output1",
                       value=self.vpc2.vpc_id)


        #VPC Peering
        self.VPCPeering = ec2.CfnVPCPeeringConnection(
            self,
            "VPCPeering",
            peer_vpc_id=self.vpc.vpc_id,
            vpc_id=self.vpc2.vpc_id,
            peer_region="eu-central-1"
        )

        for i in range(0,1):

                           self.cfn_Route = ec2.CfnRoute(self, "VPC1Route",
                           route_table_id=self.vpc.public_subnets[i].route_table.route_table_id,
                           destination_cidr_block="10.20.20.0/24",
                           vpc_peering_connection_id=self.VPCPeering.ref)
        for j in range(0,1):
                           self.cfn_Route = ec2.CfnRoute(self, "VPC2Route",
                           route_table_id=self.vpc2.public_subnets[j].route_table.route_table_id,
                           destination_cidr_block="10.10.10.0/24",
                           vpc_peering_connection_id=self.VPCPeering.ref)



        #AMI linux
        amzn_linux = ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                                 edition=ec2.AmazonLinuxEdition.STANDARD,
                                 virtualization=ec2.AmazonLinuxVirt.HVM,
                                 storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
                                    )

        #Key Pair
        key = KeyPair(self,"KeyPair",
                        name="WebServerKey",
                        store_public_key=True
                     )

        #user data to launch web server
        with open("./userdata.sh") as f:
                    user_data = f.read()



        #Mgmt server EC2 launch
        instance2 = ec2.Instance(self, "Instance2",
                    instance_type=ec2.InstanceType("t2.micro"),
                    machine_image=amzn_linux,
                    vpc = self.vpc2,
                    block_devices= [ec2.BlockDevice(
                                device_name="/dev/xvda",
                                volume=ec2.BlockDeviceVolume.ebs(
                                 volume_size=8,
                                volume_type=ec2.EbsDeviceVolumeType.GP2,
                                encrypted=True
                    ),
                    mapping_enabled= True
                     )],

        security_group = MgmtSG,
        key_name=key1.key_pair_name
        )

        #Security Group for Management Server
        MgmtSG=ec2.SecurityGroup(self,"MgmtSG", vpc= self.vpc2, allow_all_outbound=True, security_group_name="MgmtServerSG")
        MgmtSG.add_ingress_rule(ec2.Peer.ipv4("77.248.14.193/32"),
                                    ec2.Port.tcp(22),
                                    "SSH Connecton")
        MgmtSG.add_ingress_rule(ec2.Peer.ipv4("77.248.14.193/32"),
                                    ec2.Port.tcp(80),
                                    "HTTP")
        MgmtSG.add_ingress_rule(ec2.Peer.ipv4("77.248.14.193/32"),
                                    ec2.Port.tcp(443),
                                    "HTTPS")


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

              #Security Group for web server
        webSG=ec2.SecurityGroup(self,"webSG",vpc= self.vpc, allow_all_outbound=True, security_group_name="WebserverSG")
        webSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(80),
                                    "http traffic")
        webSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(443),
                                    "https traffic")
        webSG.add_ingress_rule(ec2.Peer.security_group_id(MgmtSG.security_group_id) ,
                                    ec2.Port.tcp(22),
                                       "ssh")
        webSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(socket.IPPROTO_ICMP),
                                    "ping")



        #Key Pair Mgmt Server
        key1 = KeyPair(self,"KeyPair2",
                        name="MgmtServerKey",
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