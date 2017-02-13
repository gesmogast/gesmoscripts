#!/bin/bash
# This script installs Magento2 on Ubuntu1404 system
PASSWORD='septimo'
echo "Adding mariadb repository"
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.hosteurope.de/mirror/mariadb.org/repo/10.1/ubuntu $
apt-get update
echo "Installing mariadb"
export DEBIAN_FRONTEND="noninteractive"
sudo debconf-set-selections <<< "mariadb-server mysql-server/root_password password $PASSWORD"
sudo debconf-set-selections <<< "mariadb-server mysql-server/root_password_again password $PASSWORD"
apt-get install mariadb-server mariadb-client -y
echo "Listen 0.0.0.0:3306"
sed -i "s/.*bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
echo "Configuration of Mariadb"
mysql -u root -p"$PASSWORD" < magentoinstall.sql
echo "Start mariadb"
/usr/bin/mysqld_safe
