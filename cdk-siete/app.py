#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_siete.cdk_siete_stack import CdkSieteStack



app = cdk.App()
CdkSieteStack(app, "CdkSieteStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'),
    region=os.getenv('CDK_DEFAULT_REGION'))
)

app.synth()
