# EC2 automation 

* aws configure --profile profile-name

`aws configure --profile IAC`

### AWS Cli Tricks

- list all configured profile names
`cat ~/.aws/config | grep "\[profile " | sed -e 's/\[//g' -e 's/\]//g' -e 's/profile //g'`



### NGINX CGI Conf

cp /usr/share/doc/fcgiwrap/examples/nginx.conf /etc/nginx/fcgiwrap.conf


location /cgi-bin/ {
  gzip off;
  root  /usr/lib;
  fastcgi_pass  unix:/var/run/fcgiwrap.socket;
  include /etc/nginx/fastcgi_params;
  fastcgi_param SCRIPT_FILENAME  /usr/lib$fastcgi_script_name;
}

mkdir /usr/lib/cgi-bin -p
vi /etc/nginx/sites-available/default
include fcgiwrap.conf;


server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files $uri $uri/ =404;
        }
include fcgiwrap.conf;
}

service nginx restart
pip3 install art
cd /usr/lib/cgi-bin
vi /usr/lib/cgi-bin/test.py


#!/usr/bin/python3
from art import *
Art=text2art("TEST",font='block',chr_ignore=True)
print('Content-Type: text/plain')
print('')
print('This is my test!')
print(Art)


chmod 755 /usr/lib/cgi-bin/test.py