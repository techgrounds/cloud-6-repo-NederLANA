#!/bin/bash
 yum -y install httpd
 systemctl enable httpd
 systemctl start httpd
 echo '<html><h1>Hi, Techgrounds. Hello, Sentia!</h1></html>' > /var/www/html/index.html