import aws_cdk as core
import aws_cdk.assertions as assertions

from ecs_project.ecs_project_stack import EcsProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ecs_project/ecs_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EcsProjectStack(app, "ecs-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
