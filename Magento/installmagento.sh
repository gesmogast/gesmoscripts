#!/bin/bash
PASSWORD='septimo'
HOSTNAME='testmagento.org'
IP=`ip addr show | grep global | awk '{print $2}' | cut -d "/" -f1`
SPACE=" "
HOSTS=$IP$SPACE$HOSTNAME
echo $HOSTS >> /etc/hosts
echo "Creating install dir"
mkdir -p /home/install
cd /home/install
echo "Installing PHP7"
wget https://www.dotdeb.org/dotdeb.gpg
echo -e "deb http://packages.dotdeb.org jessie all\ndeb-src http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list
gpg --keyserver keyserver.ubuntu.com --recv E9C74FEEA2098A6E
gpg -a --export E9C74FEEA2098A6E | apt-key add -
echo "Installing nginx and installation dependencies"
apt-get install -y nginx software-properties-common
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
echo "Adding mariadb repository"
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mariadb.mirror.triple-it.nl/repo/10.1/debian jessie main'
apt-get update
echo "Installing php7"
apt-get install php7.0-fpm php7.0-mcrypt php7.0-curl php7.0-cli php7.0-mysql php7.0-gd php7.0-xsl php7.0-json php7.0-intl php-pear php7.0-dev php7.0-common php7.0-mbstring php7.0-zip php-soap libcurl3 curl -y
echo "Installing mariadb"
export DEBIAN_FRONTEND="noninteractive"
sudo debconf-set-selections <<< "mariadb-server mysql-server/root_password password $PASSWORD"
sudo debconf-set-selections <<< "mariadb-server mysql-server/root_password_again password $PASSWORD"
apt-get install mariadb-server mariadb-client -y
echo "Configuration of Mariadb"
cd /home
mysql -u root -p"$PASSWORD" < magentoinstall.sql
echo "Installing composer"
curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/bin/composer
cd /var/www/
wget https://github.com/magento/magento2/archive/2.1.3.tar.gz
tar -xzf /var/www/2.1.3.tar.gz
mv magento2-2.1.3/ magento
cd /var/www/magento
echo "Composer install dependencies magento"
composer install -v
cd /home
echo "Removing default nginx configuration"
rm /etc/nginx/sites-available/default
echo "Install nginx magento config"
cp magento.conf /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/magento.conf /etc/nginx/sites-enabled/
echo "Restarting nginx"
service nginx restart
echo "Installing Magento2"
/var/www/magento/bin/magento setup:install --backend-frontname="admin" \
--key="biY8vdWx4w8KV5Q59380Fejy36l6ssUb" \
--db-host="localhost" \
--db-name="magentodb" \
--db-user="magento" \
--db-password="septimo" \
--language="en_US" \
--currency="USD" \
--timezone="America/New_York" \
--use-rewrites=1 \
--use-secure=0 \
--base-url="http://testmagento.org" \
--base-url-secure="https://testmagento.org" \
--admin-user=admin \
--admin-password=ABCdefg123! \
--admin-email=admin@testmagento.org \
--admin-firstname=admin \
--admin-lastname=user \
--cleanup-database
echo "Configuring website permissions"
chmod 700 /var/www/magento/app/etc
chown -R www-data:www-data /var/www/magento
service nginx restart
