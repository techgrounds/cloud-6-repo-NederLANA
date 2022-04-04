#!/bin/bash
 yum -y install httpd
 systemctl enable httpd
 systemctl start httpd
 echo '<html><h1>I would like to take this moment to thank all my classmates for pushing and pulling me through the TG course. And thank Sentia for giving me an opportunity to use what I have learned!</h1></html>' > /var/www/html/index.html