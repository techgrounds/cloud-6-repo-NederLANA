import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_diez.cdk_diez_stack import CdkDiezStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_diez/cdk_diez_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkDiezStack(app, "cdk-diez")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
