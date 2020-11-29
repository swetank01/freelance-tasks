#!/bin/bash
sudo apt -y update

echo "Install git"
apt install -y git

echo "Install python3"
apt-get -y install python3 python3-pip python3-dev

echo "Install Docker engine"
apt update -y
apt install docker docker-compose -y
sudo usermod -a -G docker 
sudo service docker start
sudo chkconfig docker on

echo "Install Nginx and CGI"
apt-get -y install nginx fcgiwrap uwsgi