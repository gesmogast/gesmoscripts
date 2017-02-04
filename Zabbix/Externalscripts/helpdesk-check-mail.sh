#!/bin/bash
#Проверка наличия файлов старше 10 минут в почтовой папке helpdesk
FOLD='/mnt/helpdeskmailfolder/'
RESULT=$(find $FOLD -maxdepth 1 -mmin +10 -type f \( -name "*.msg" \) | wc -l )
echo $RESULT


