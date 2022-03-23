import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_siete.cdk_siete_stack import CdkSieteStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_siete/cdk_siete_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkSieteStack(app, "cdk-siete")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
