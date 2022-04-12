"""
Nested stacks to modularize how stacks are built and deployed.
Each stack is decoupled and easier to modify without disrupting
the entire infrastructure.

This limits down time of the entire system while one component is being backed up.

Here a main stack is built upon which all the nested stacks are called.
"""


#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_ocho.ecs_patterns import EcsPatterns
from cdk_ocho.admin import Admin
#from cdk_ocho.peering import Peering
from cdk_ocho.security import Security
from cdk_ocho.backups import Backups
from cdk_ocho.roles import Roles



app = cdk.App()
root_stack = cdk.Stack(
    app, "RootStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'),
    region=os.getenv('CDK_DEFAULT_REGION'))
)

ecs_patterns = EcsPatterns(root_stack, "EcsPatterns")

admin_server = Admin(root_stack, "AdminServer")

#vpc_peering = Peering(root_stack, "VpcPeering")

i_am_roles = Roles(root_stack, "Roles")

security_groups = Security(root_stack, "Security")

back_ups = Backups(root_stack, "Backups" )

app.synth()
