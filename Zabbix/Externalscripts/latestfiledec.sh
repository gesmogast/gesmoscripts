#!/bin/bash
#Количество часов с момента создания архива
FOLD=$1
LETTER=$2
FILE=`ls -t1 $FOLD | sort -r | head -n4 | grep $LETTER | tail -n 1`
NOW=`date +%s`
OLD=`stat -c %Z $FOLD/$FILE`
AGE=$(((NOW-OLD)/3600))
echo $AGE
