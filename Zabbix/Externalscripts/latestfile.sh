#!/bin/bash
#Количество часов с момента создания архива
OLD_IFS=$IFS
IFS=$'\n'
FOLD=$1
FILE=`ls -t1 $FOLD | sort -r | head -n1`
NOW=`date +%s`
OLD=`stat -c %Z $FOLD/$FILE`
AGE=$(((NOW-OLD)/3600))
echo $AGE
IFS=$OLD_IFS
