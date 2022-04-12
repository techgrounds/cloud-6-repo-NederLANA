#!/bin/bash
 yum -y install httpd
 systemctl enable httpd
 systemctl start httpd
 echo '<html><h1>I would like to thank all my classmates for pushing and pulling me through the tough parts! And to thank Sentia for giving me an opportunity to be able to use what I learned.</h1></html>' > /var/www/html/index.html