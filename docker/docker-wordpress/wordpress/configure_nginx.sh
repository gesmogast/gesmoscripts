#!/bin/bash
# This script installs Mariadb on Ubuntu 16.04 system
apt-get update
apt-get install php-curl php-gd php-mbstring php-mcrypt php-xml php-xmlrpc php-fpm php-mysql -y
service php7.0-fpm restart
cd /tmp
curl -O https://wordpress.org/latest.tar.gz
tar xzf latest.tar.gz
cp /tmp/wordpress/wp-config-sample.php /tmp/wordpress/wp-config.php
mkdir /tmp/wordpress/wp-content/upgrade
mkdir -p /var/www/wordpress
cp -a /tmp/wordpress/. /var/www/wordpress
# Configuring permissions
chown -R www-data:www-data /var/www/html
find /var/www/wordpress -type d -exec chmod g+s {} \;
chmod g+w /var/www/wordpress/wp-content
chmod -R g+w /var/www/wordpress/wp-content/themes
chmod -R g+w /var/www/wordpress/wp-content/plugins
