from aws_cdk import (
    NestedStack,
    CfnOutput,
    aws_ec2 as ec2,
)
from constructs import Construct

class PeeringNStack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Peering between VPC1 and VPC2
        self.VPCPeering=ec2.CfnVPCPeeringConnection(
            self,
            "VPCPeering",
            peer_vpc_id=self.vpc1.vpc_id,
            vpc_id=self.vpc2.vpc_id,
            peer_region="eu-central-1")

        for i in range(0,1):
            self.cfn_Route=ec2.CfnRoute(self, "VPCwRouteVPCa",
            route_table_id=self.vpc1.public_subnets[i].route_table.route_table_id,
            destination_cidr_block="10.20.20.0/24",
            vpc_peering_connection_id=self.VPCPeering.ref)

        for j in range(0,1):
            self.cfn_Route=ec2.CfnRoute(self, "VPCaRouteVPCw",
            route_table_id=self.vpc2.public_subnets[j].route_table.route_table_id,
            destination_cidr_block="10.10.10.0/24",
            vpc_peering_connection_id=self.VPCPeering.ref)