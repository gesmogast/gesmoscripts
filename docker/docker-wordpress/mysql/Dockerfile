FROM rastasheep/ubuntu-sshd:16.04
MAINTAINER armagast@gmail.com
# Installation of mariadb

RUN apt-get update && apt-get install -y openssh-server supervisor
RUN mkdir -p /var/run/sshd /var/log/supervisor
COPY supervisord.conf /etc/supervisor/supervisord.conf

ADD install_mariadb.sh /home/

RUN ["chmod","+x","/home/install_mariadb.sh"] 
RUN /home/install_mariadb.sh && rm /home/install_mariadb.sh 

#RUN mkdir /var/lib/mysql

EXPOSE 22 3306

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
