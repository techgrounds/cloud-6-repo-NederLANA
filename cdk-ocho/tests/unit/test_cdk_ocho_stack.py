import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_ocho.cdk_ocho_stack import CdkOchoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_ocho/cdk_ocho_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkOchoStack(app, "cdk-ocho")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
