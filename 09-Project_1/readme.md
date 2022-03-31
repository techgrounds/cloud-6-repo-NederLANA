# Installing AWS CDK

An AWS CDK app is an application written in TypeScript, JavaScript, Python, Java, or C# that uses the AWS CDK to define AWS infrastructure. An app defines one or more stacks. Stacks (equivalent to AWS CloudFormation stacks) contain constructs, each of which defines one or more concrete AWS resources, such as Amazon S3 buckets, Lambda functions, Amazon DynamoDB tables, and so on.

Constructs (as well as stacks and apps) are represented as classes (types) in your programming language. You instantiate constructs within a stack to declare them to AWS, and connect them to each other using well-defined interfaces.

The AWS CDK includes the CDK Toolkit (also called the CLI), a command-line tool for working with your AWS CDK apps and stacks. Among other functions, the Toolkit provides the ability to convert one or more AWS CDK stacks to AWS CloudFormation templates and related assets (a process called synthesis) and to deploy your stacks to an AWS account.

The AWS CDK includes a library of AWS constructs called the AWS Construct Library, organized into various modules. The library contains constructs for each AWS service. The main CDK package is called aws-cdk-lib, and it contains the majority of the AWS Construct Library, along with base classes like Stack and App used in most CDK applications.

The actual package name of the main CDK package varies by language.

Finally, the constructs package contains the Construct base class. It's in its own package because it is used not only by the AWS CDK but also by other construct-based tools, including CDK for Terraform and CDK for Kubernetes.


### 1) Prerequisites to install and use the AWS CDK with Python.
- All AWS CDK developers, even those working in Python, Java, or C#, **need Node.js 10.13.0 or later**. All supported languages use the same back end, which runs on Node.js. We recommend a version in active long-term support, which, at this writing, is the latest 16.x release. (done)
- Install AWS CLI
- You must configure your workstation with your credentials and an AWS region. If you have the AWS CLI installed, the easiest way to satisfy this requirement is issue the following command:
- >$aws configure
- Provide your AWS access key ID, secret access key, and default region when prompted.
- Install Python 3.6 or later including pip and virtualenv

### 2) Now Install the AWS CDK
- Install the AWS CDK Toolkit globally using the following Node Package Manager command.
$npm install -g aws-cdk

### 3) Bootstrapping
Many AWS CDK stacks that you write will include assets: external files that are deployed with the stack, such as AWS Lambda functions or Docker images. The AWS CDK uploads these to an Amazon S3 bucket or other container so they are available to AWS CloudFormation during deployment. Deployment requires that these containers already exist in the account and region you are deploying into. Creating them is called bootstrapping. To bootstrap, issue:
$cdk bootstrap aws://ACCOUNT-NUMBER/REGION

### 4) AWS CDK tools (done)
The AWS CDK Toolkit, also known as the Command Line Interface (CLI), is the main tool you use to interact with your AWS CDK app. It executes your code and produces and deploys the AWS CloudFormation templates it generates.
- The AWS Toolkit for Visual Studio Code is an open-source plug-in for Visual Studio Code that makes it easier to create, debug, and deploy applications on AWS. The toolkit provides an integrated experience for developing AWS CDK applications, including the AWS CDK Explorer feature to list your AWS CDK projects and browse the various components of the CDK application. **Install the plug-in**





## Key-terms


## Assignment


### References
https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html

https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html#setup-prereq

https://towardsthecloud.com/how-to-set-up-aws-cdk

cdk tutorial: be a better dev
https://www.youtube.com/watch?v=I2cXlYYoQqQ

Update pip in Python:
https://www.youtube.com/watch?v=VhOhojy0b28

Instal virtualenv in pip:
https://www.youtube.com/watch?v=N5vscPTWKOk

npm install error fix:
https://medium.com/illumination/how-to-fix-npm-audit-error-with-loadvirtual-and-enolock-deprecated-dependencies-1f07ba65eef9

cdk running scripts disabled error fix:
https://www.youtube.com/watch?v=K8CPnfbiWTc

install AWS CLI in Windows:
https://www.youtube.com/watch?v=jCHOsMPbcV0&t=12s

configure AWS CLI in terminal:
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html

cdk init:
https://bobbyhadz.com/blog/aws-cdk-init
https://bobbyhadz.com/blog/aws-cdk-tutorial-typescript

cdk crash course:
https://www.youtube.com/watch?v=T-H4nJQyMig

cdk commands to use in python:
https://docs.aws.amazon.com/cdk/v1/guide/work-with-cdk-python.html

import cdk library to python bin:
- >$import aws_cdk as cdk
https://cto.ai/blog/create-and-deploy-a-sample-cdk-application-2/

sample aws cdk scripts to deploy resources:
https://github.com/aws-samples/aws-cdk-examples/tree/master/python

CLI security restrictions from single IP address:
https://www.youtube.com/watch?v=EA1bHXK_LHw

Assign IAM Roles for user to access Cloudformation from restricted IP:
- https://aws.amazon.com/premiumsupport/knowledge-center/iam-restrict-calls-ip-addresses/#
- https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam-readme.html

Set up SSH to private VPC resources via Systems Manager:
https://aws.amazon.com/premiumsupport/knowledge-center/systems-manager-ssh-vpc-resources/

SG and SSH from specific IP for VPC:
https://www.pulumi.com/docs/guides/crosswalk/aws/vpc

socket pairs connecting server/client:
https://levelup.gitconnected.com/operating-system-concepts-sockets-a78ddb9b5f9c

aws cdk vpc:
https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html

aws cdk github examples:
https://github.com/aws-samples/aws-cdk-examples

aws cdk reference documentation:
https://docs.aws.amazon.com/cdk/v2/guide/home.html

aws cdk v2 Construct Hub:
https://constructs.dev/search?q=&cdk=aws-cdk&cdkver=2&sort=downloadsDesc&offset=0

multiple stacks:
- https://bobbyhadz.com/blog/create-multiple-stacks-aws-cdk
- https://docs.aws.amazon.com/cdk/v2/guide/stack_how_to_create_multiple_stacks.html

nested stacks:
- https://cfn101.workshop.aws/intermediate/templates/nested-stacks.html
- https://www.youtube.com/watch?v=Y_XQ7WT-WcA
- https://aws.amazon.com/blogs/devops/use-nested-stacks-to-create-reusable-templates-and-support-role-specialization/
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-nested-stacks.html

passing value from stack1 to stack2:
https://aws.amazon.com/premiumsupport/knowledge-center/cloudformation-nested-stacks-values/

create cloud formation templates:
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html

lambda to look up vpc information:
https://aws.amazon.com/blogs/mt/looking-up-information-on-aws-cloudformation-stack-parameters-using-aws-lambda/

parameters:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html

backups:
- https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_backup.html
- https://pypi.org/project/aws-cdk.aws-backup/
- https://www.cdw.com/content/cdw/en/articles/cloud/deleting-aws-backup-vaults-recovery-points-at-scale.html

backup resource ARN:
- https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#aws-managed-policies

cdk python:
- https://aws.amazon.com/blogs/developer/getting-started-with-the-aws-cloud-development-kit-and-python/
- https://pypi.org/project/aws-cdk-lib/

aws cdk github:
https://github.com/aws/aws-cdk

python cdk examples github:
https://github.com/aws-samples/aws-cdk-examples/tree/master/python

constructs hub:
https://constructs.dev/search?q=&cdk=aws-cdk&cdkver=2&langs=python&sort=downloadsDesc&offset=0

building stacks:
https://constructs.dev/packages/aws-cdk-lib/v/2.15.0?lang=typescript

deploying nested stacks:
https://blog.shikisoft.com/cloudformation-nested-stacks-codepipeline/

parameters:
https://pypi.org/project/cdk-resources/

setting up iam roles from constructs lib:
https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam-readme.html

systems manager IAM role to access web server:
- https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html
- https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_service-with-iam.html

including cloudformation in template:
https://pypi.org/project/aws-cdk.cloudformation-include/

https://pypi.org/project/aws-cdk-lib/

cdk basics:
https://www.youtube.com/watch?v=SbOmvNe1s8k&t=224s

context and env variables instead of parameters:
- https://awsmaniac.com/how-to-parametrize-our-aws-cdk-stacks/
- https://docs.aws.amazon.com/cdk/v2/guide/context.html
- https://docs.aws.amazon.com/cdk/v2/guide/get_context_var.html

rupali's recommended github example:
https://github.com/miztiik/my-first-cdk-project

setting environment variable upon deployment of stacks:
https://yshen4.github.io/infrastructure/AWS/CDK_context.ht

delete recovery/backup fault:
- https://cloudonaut.io/aws-backup-vault-cannot-be-deleted-use-this-script/
- https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-a-vault.html

---
ecs pattern construct:
- https://docs.aws.amazon.com/cdk/v2/guide/ecs_example.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-ecs-web-server-cdk.html

redirect http to https using alb:
- https://aws.amazon.com/premiumsupport/knowledge-center/elb-redirect-http-to-https-using-alb/
- https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_elasticloadbalancingv2/README.html

self sign certificiate:
- https://zuqqhi2.com/en/generating-self-signed-certificate-and-applying-to-aws-alb

create self signed certificate during cloudformation:
- https://pillpall.github.io/aws/2020/08/27/Create-Self-Signed-Certificate-with-Cloudformation.html

acm certificate manager:
- https://docs.aws.amazon.com/code-samples/latest/catalog/python-acm-certificate_basics.py.html

tls 1.2 required
https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-fips-endpoints/

https ec2 public ip with no domain
- https://bansalanuj.com/https-aws-ec2-without-custom-domain

### Issues


### Results

**Prereq to installing AWS CDK:**

In windows:
- Installed node.js
- Installed AWS CDK Tools for Visual Studio Code (includes AWS CLI)
- Prompted by Python to update pip. Must cd to directory of Python310:
- >$cd AppData\Local\Programs\Python\Python310
- >$python -m pip install --upgrade pip
- Install virtualenv (so each python project is in its own dev environment with its own settings=more resilient). Run:
- >$pip install virtualenv
- **Install AWS CLI** (from windows terminal), run:
- >$aws configure (input access key ID and secret access key assigned to IAM user (Q), and default region eu-central-1)
- Bootstrap IAM user: Q so that cdk can deploy resources to it. From windows terminal, run:
- >$aws sts get-caller-identity
- >$cdk bootstrap aws://ACCOUNT-NUMBER/REGION (acct# returned from previous command, region eu-central-1)

**AWS CDK install and configure:**

- Use node.js to install cdk globally. Run:
- >$npm install -g aws-cdk
- Error resolved: 1 vulnerability (about separating project environments) by running following:
- >$npm i --package-lock-only
- >$npm config get package-lock
- >$npm config get shrinkwrap
- >$npm audit fix
- Error resolved: running scripts disabled on system, by opening Powershell as admin, and running:
- >$Get-ExecutionPolicy (default is restricted)
- >$Set-ExecutionPolicy Unrestrict (only globally unrestricted for purpose of this project. Otherwise use least privilege and perhaps only unrestrict the script itself)
- >$python -m pip install aws-cdk-lib (where most aws cdk constructs are stored, except experimental modules. Here it is installed in windows terminal under python310 subfolder, for all python scripts. Remember to install specific modules in project folder)

**Connect aws cdk to AWS:**
- In VS Code, click on aws plug-in from left sidebar and connect to AWS using default profile.
---

**Normally deploy with cdk for a blank project:**
- >$cdk init app --language python

Test deploy a project to explore cdk within python terminal:
Part 1)
- >$mkdir cdk-demo
- >$cd cdk-demo
- >$cdk init sample-app --language python (Initialize cdk project with language of choice. This also installs all packages needed for project.)
- When application is done initializing, open it in VSC. In the editor, the bin directory houses application resources. It imports the core libraries, creates a new application, and imports the stack.
- >#$.\source .venv/bin/activate (After initializing the project, activate the project's virtual environment whenever you start working on it. This allows the project's dependencies to be installed locally in the project folder, instead of globally.)
- >$python -m pip install -r requirements.txt (After activating virtual environment for the first time, install the app's standard dependencies. **AND** after installing a module, to update project's requirements.txt file.)
- Error resolved: aws plug-in (under CDK Preview) says "unable to load construct tree for this App, Run 'cdk synth'):
- >$cdk synth (returned msg to run: cdk bootstrap)
- >$cdk bootstrap aws://ACCOUNT-NUMBER/REGION (bootstrap environment again to connect to AWS) (Ignore message and continue on with your life: CDK bootstrap stack version 6 required. Please run 'cdk bootstrap' with a recent version of the CDK CLI)

Part 2)
- create s3 bucket (add new dependency under cdk_demo_stack.py):
- >aws_s3 as s3, (define and name bucket under stack code block, which will then be executed by app.py)

Part 3)
- now compile local code to Cloudformation:
- >$cdk synth
- >$cdk deploy

---

### Errors

- "Failed to publish one or more assets"
- https://ketuma.com/blog/cdk-bootstrap-error-and-how-to-fix-it/
- "AttributeError: type object 'module' has no attribute"



### Extra Features
- You may optionally use the --role-arn (or -r) option to specify the ARN of an IAM role that should be used for deployment. This role must be assumable by the AWS account being used.
- https://docs.aws.amazon.com/cdk/v2/guide/cli.html




