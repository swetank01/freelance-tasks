# Docker compose with nginx 

## Task Description (given by author)
We configure a application with docker-compose
while we are assigning a SSL certificates in nginx. I'm facing issue.
Need a support on docker and nginx

#### Skills Required
- nginx 
- docker
- ubuntu

#### Link
[Truelance link](https://www.truelancer.com/freelance-project/docker-compose-with-nginx-256550?utm_source=job_posting_notification&utm_medium=email&utm_campaign=Notifications)

## Step to follow 

1. Generate ssl certs using openssl
- `cd nginx-ssl-certs`
- `sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx-selfsigned.key -out nginx-selfsigned.crt`
- hint -> add passphase

2. Create 'nginx.conf' file and place it in directory
- `cd nginx-conf`
```
server {
    listen 443 ssl;
    server_name  freelance.farnodes.com;
    ssl_certificate /etc/nginx/certs/nginx-selfsigned.crt;
    ssl_certificate_key /etc/nginx/certs/nginx-selfsigned.key;
    
    location / {
        error_log /var/log/front_end_errors.log;
    }
}
```

3. Build and Run 
- `docker-compose build`
- `docker-compose up -d`