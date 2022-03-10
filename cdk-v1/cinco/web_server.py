from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    NestedStack,
    aws_cloudformation as cfn,
     CfnOutput,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_kms as kms,
    aws_events as events,
    aws_iam as iam,
)

class WebServer(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        instance1 = ec2.Instance(self, web_instance_id,
                                    instance_type=ec2.InstanceType(web_instance_type),
                                    machine_image=amzn_linux,
                                    vpc = self.vpc,
                                     block_devices= [ec2.BlockDevice(
                                    device_name="/dev/xvda",
                                     volume=ec2.BlockDeviceVolume.ebs(
                                                                     volume_size= web_volume_size,
                                                                     volume_type=ec2.EbsDeviceVolumeType.GP2,
                                                                     encrypted=True
                                                                      ),
                                     mapping_enabled= True
                                       )
                                                ],
                                 user_data=ec2.UserData.custom(user_data),
                                 role=role1,
                                  security_group = webSG,
                                  key_name=key.key_pair_name
        )
        instance1.connections.allow_from_any_ipv4(port_range=ec2.Port.tcp(80)
                                                  , description="Allow Web Traffic")



        CfnOutput(self,"ip", value=str(instance1.instance_private_ip))

      #Network access control list (NACL)

        aclcidr1= ec2.AclCidr.any_ipv4()
        nacl=ec2.NetworkAcl(self,"mynacl",vpc=self.vpc2)
        nacl.add_entry("id",cidr=aclcidr1,rule_number=100,
               traffic=ec2.AclTraffic.all_traffic(),direction=ec2.TrafficDirection.EGRESS,
                  network_acl_entry_name="myentry",rule_action=ec2.Action.ALLOW)