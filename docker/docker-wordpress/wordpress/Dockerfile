FROM rastasheep/ubuntu-sshd:16.04
MAINTAINER armagast@gmail.com
# Installation of wordpress

RUN apt-get update && apt-get install -y supervisor nginx curl
RUN mkdir -p /var/log/supervisor /var/run/php
COPY supervisord.conf /etc/supervisor/supervisord.conf

COPY wordpress.conf /etc/nginx/sites-available/
RUN ln -s  /etc/nginx/sites-available/wordpress.conf /etc/nginx/sites-enabled/ && rm /etc/nginx/sites-available/default && unlink /etc/nginx/sites-enabled/default

ADD configure_nginx.sh /home/
RUN ["chmod","+x","/home/configure_nginx.sh"]
RUN /home/configure_nginx.sh && rm /home/configure_nginx.sh

RUN rm /var/www/wordpress/wp-config.php
ADD wp-config.php /var/www/wordpress/

EXPOSE 22 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
