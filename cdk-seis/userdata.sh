#!/bin/bash
 yum -y install httpd
 systemctl enable httpd
 systemctl start httpd
 echo '<html><h1><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeuRmTb0FiTiZJz-7mnKS6tNjdW9Gk5ErfNz2cDUBK6LnJ7YQ/viewform?embedded=true" width="640" height="1141" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe></h1></html>' > /var/www/html/index.html
