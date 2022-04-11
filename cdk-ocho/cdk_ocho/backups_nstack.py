from aws_cdk import (
    NestedStack,
    Tags
    RemovalPolicy,
    Tags,
    aws_ec2 as ec2,
    aws_backup as backup,
    aws_events as events,
    aws_iam as iam,
    aws_ssm as ssm,
    CfnOutput,
    aws_ec2 as ec2,
)
from constructs import Construct

class BackupsNstack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


#server Tags
        Tags.of(instance1).add(key="webs",value="WebBackup")
        Tags.of(instance2).add(key="admins",value="AdminBackup")

        #Back up Web Server
        vault1=backup.BackupVault(
            self,"webvault",
            backup_vault_name="webvault",
            removal_policy=RemovalPolicy.DESTROY
        )
        backup_plan1=backup.BackupPlan(
            self,"Backup1",
            backup_plan_name="WebBackup"
        )
        backup_plan1.add_selection(
            "ebsResource",
            resources=[
                backup.BackupResource.from_tag(
                    key="webs",value="WebBackup")])

        backup_plan1.add_rule(
            backup.BackupPlanRule(
                backup_vault=vault1,
                rule_name="WebRule",
                schedule_expression=events.Schedule.cron(
                    hour="7",
                    minute="00",
                    day="*",
                    month="*",
                    year="*"
                ),
                delete_after=Duration.days(7),
                completion_window=Duration.hours(2),
                start_window=Duration.hours(1)
            )
        )

        #Back-up for Admin Server
        vault2= backup.BackupVault(
            self,"adminvault",
            backup_vault_name="adminvault",
            removal_policy=RemovalPolicy.DESTROY
        )
        backup_plan2=backup.BackupPlan(
            self,"Backup2",
            backup_plan_name="AdminBackup"
        )
        backup_plan2.add_selection(
            "ebsResource1",
            resources=[
                backup.BackupResource.from_tag(
                    key="admins",value="AdminBackup")])

        backup_plan2.add_rule(
            backup.BackupPlanRule(
                backup_vault=vault2,
                              rule_name="AdminRule",
                              schedule_expression=events.Schedule.cron(
                                  hour="7" ,
                                  minute="00",
                                  day="*",
                                  month="*",
                                  year="*"
                              ),
                              delete_after=Duration.days(7),
                              completion_window=Duration.hours(2),
                              start_window=Duration.hours(1)
                              )
                )