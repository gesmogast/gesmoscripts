#!/bin/bash
OLD_IFS=$IFS
IFS=$'\n'
FOLD=$1
FILE=`ls -t1 $FOLD | sort -r | head -n1`
echo $FILE
IFS=$OLD_IFS
