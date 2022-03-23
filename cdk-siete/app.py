#!/usr/bin/env python3
import os
import this

import aws_cdk as cdk

#from cdk_siete.cdk_siete_stack import CdkSieteStack
from cdk_siete.server_web import ServerWeb
from cdk_siete.server_admin import ServerAdmin


app = cdk.App()
#main_stack = (app, 'MainStack', env={'region': 'eu-central-1'},
#ServerWeb = ServerWeb(
    #main_stack,
    #'ServerWeb'
#)
ServerWeb(app, "ServerWeb")
ServerAdmin(app, "ServerAdmin")
#CdkSieteStack(app, "CdkSieteStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html


app.synth()
