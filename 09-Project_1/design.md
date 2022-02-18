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
- You must configure your workstation with your credentials and an AWS region. If you have the AWS CLI installed, the easiest way to satisfy this requirement is issue the following command: $aws configure
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






Lists of questions for theoretical research:
What is X for?
How does X fit / replace X in a classical setting?
How can X be combined with other services?
What is the difference between X and other similar programs?



## Key-terms


## Assignment


### References
https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html

https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html#setup-prereq

https://towardsthecloud.com/how-to-set-up-aws-cdk

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





### Issues


### Results

**Prereq to installing AWS CDK:**

- Installed node.js
- Installed AWS CDK Tools for Visual Studio Code (includes AWS CLI)
- Prompted by Python to update pip. Must cd to correct directory of Python310 and run
- >$python -m pip install --upgrade pip
- Install virtualenv (so each python project is in its own dev environment with its own settings=more resilient).
- >$pip install virtualenv
- Install AWS CLI (from windows terminal)
- >$aws configure (input access key ID and secret access key assigned to IAM user (Q), and default region eu-central-1)
- Bootstrap IAM user: Q so that cdk can deploy resources to it. (from windows terminal)
- >$aws sts get-caller-identity
- >$cdk bootstrap aws://ACCOUNT-NUMBER/REGION (acct# returned from previous command, region eu-central-1)

**AWS CDK install:**

- Use node.js to install cdk globally. Run $npm install -g aws-cdk
- Error: resolved: 1 vulnerability (about project environment) by running following:
- >$npm i --package-lock-only
- >$npm config get package-lock
- >$npm config get shrinkwrap
- >$npm i --package-lock-only
- >$npm audit fix
- Error resolved: running scripts disabled on system, by opening Powershell as admin, and running:
- >$Get-ExecutionPolicy (default is restricted)
- >$Set-ExecutionPolicy Unrestrict (only globally unrestricted for purpose of this project. Otherwise use least privilege and perhaps only unrestrict the script itself)

**Connect aws cdk to AWS:**
- In VS Code, click on aws plug-in from sidebar and connect to AWS using default profile.
---

Test deploy with cdk for a blank project:
- >$cdk init app --language python

First deploy a test project to explore cdk:
- >$mkdir cdk-demo && cd cdk-demo
- >$cdk init sample-app --language python


