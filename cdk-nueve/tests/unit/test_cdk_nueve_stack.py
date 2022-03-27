import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_nueve.cdk_nueve_stack import CdkNueveStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_nueve/cdk_nueve_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkNueveStack(app, "cdk-nueve")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
