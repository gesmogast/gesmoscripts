#!/bin/bash
# Asterisk сервер
server="root@ip"
# Уникальная метка
ts=$(date +%s%N)
# Создаем два файла
txtname=/tmp/zabbix-alert.$ts.txt
callname=/tmp/zabbix-alert.$ts.call
# Наговариваемый текст. #
# Приветствие. Запятые для паузы.
echo "Внимание" > $txtname
# $2 - subject триггера. Можно поставить $3 - сообщение.
echo "$2" >> $txtname
# Call-файл Asterisk
echo "Channel: Local/$1@plan-zabbix" > $callname
echo "Extension: s" >> $callname
echo "MaxRetries: 1" >> $callname
echo "RetryTime: 60" >> $callname
echo "WaitTime: 30" >> $callname
# С какого номера звоним
echo "Callerid: 123" >> $callname
#echo "Password: 123" >> $callname
echo "Application: Playback" >> $callname
# Повторяем 3 раза
echo "Data: /var/lib/asterisk/sounds/zabbix-alert.$ts&/var/lib/asterisk/sounds/zabbix-alert.$ts&/var/lib/asterisk/sounds/zabbix-alert.$ts" >> $callname
#scp $txtname $server:$txtname
scp $callname $server:$callname
#rm -f $txtname
rm -f $callname
cat $txtname | /usr/bin/text2wave -F 8000 -eval '(voice_msu_ru_nsh_clunits)' > /tmp/zabbix-alert.$ts.wav
rm -f $txtname
scp /tmp/zabbix-alert.$ts.wav $server:/var/lib/asterisk/sounds/zabbix-alert.$ts.wav
ssh $server "chown -R asterisk:asterisk /var/lib/asterisk/sounds/zabbix-alert* && chmod -R 777 /var/lib/asterisk/sounds/zabbix-alert* && mv $callname /var/spool/asterisk/outgoing/ &&  find /var/spool/asterisk/outgoing/ -name 'zabbix-alert*' -type f -mmin +10 -delete && find /var/lib/asterisk/sounds/ -name 'zabbix-alert*' -type f -mmin +10 -delete"
