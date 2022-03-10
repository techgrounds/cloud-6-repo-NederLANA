#!/usr/bin/env python3

import aws_cdk as cdk

from cinco.vpc_nstack import VpcNstack


app = cdk.App()

MainStack(app, "MainStack)")

VpcNstack(app, "vpc1")
VpcNstack(app, "vpc2")

app.synth()
