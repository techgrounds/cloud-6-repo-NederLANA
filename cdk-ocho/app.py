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

from cdk_ocho.cdk_ocho_stack import CdkOchoStack
from cdk_ocho.admin_nstack import AdminNstack



app = cdk.App()
main_stack = cdk.Stack(
    app, "MainStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'),
    region=os.getenv('CDK_DEFAULT_REGION'))
)

cdk_ocho_stack = CdkOchoStack(main_stack, "CdkOchoStack")

admin_nstack = AdminNstack(main_stack, "AdminStack")


app.synth()
