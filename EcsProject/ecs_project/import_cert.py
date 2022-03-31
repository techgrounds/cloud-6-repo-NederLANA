"""
AWS Cloudformation allows you to create self-signed certificates
during the stack creation process which you can then use to
attach it to other AWS resources like an ELB.

https://pillpall.github.io/aws/2020/08/27/Create-Self-Signed-Certificate-with-Cloudformation.html

add cert to alb:
const certificateArn = "arn:aws:acm:....;
const listenerPort443 = alb.addListener('listenerPort443', { port: 443, });
listenerPort443.addCertificateArns('SSL', [ certificateArn ]);

"""

import boto3  #Python AWS SDK package. Have to store/manage deployed resources yourself.
import PCA_cert
from os.path import exists

def generated_certificate():
    if exists("arn.txt"):
        f = open("arn.txt", "r+")
        return f.read()
    else:
        acm = boto3.client('acm')
        response = acm.import_certificate(
            Certificate=PCA_cert.certifictate_pem,
            PrivateKey=PCA_cert.private_key_pem,
            CertificateChain=PCA_cert.ca_certifictate_pem,
        )
        arn = response['CertificateArn']
        f = open("arn.txt", "w+")
        f.write(arn)

        return arn