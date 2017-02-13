#!/bin/bash
# This script installs Magento2 on Ubuntu1404 system
PASSWORD='septimo'
echo "Adding mariadb repository"
apt-get install software-properties-common -y
echo "Install MariaDB repository key"
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
echo "Add MariaDB repository"
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.hosteurope.de/mirror/mariadb.org/repo/10.1/ubuntu xenial main'
apt-get update
echo "Installing mariadb"
export DEBIAN_FRONTEND="noninteractive"
debconf-set-selections <<< "mariadb-server mysql-server/root_password password $PASSWORD"
debconf-set-selections <<< "mariadb-server mysql-server/root_password_again password $PASSWORD"
apt-get install mariadb-server mariadb-client -y
echo "Changing my.cnf to listen 0.0.0.0:3306"
sed -i "s/.*bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
