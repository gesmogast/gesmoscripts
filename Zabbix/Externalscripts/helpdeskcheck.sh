#!/bin/bash
#Проверка наличия UP в текстовом файле /mnt/helpdesk/helpdesk.txt
FOLD=$1
F1=`cat $FOLD`
RESULT=$(expr index "$F1" 'Up')
echo $RESULT


