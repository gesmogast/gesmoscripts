#!/bin/bash
OLD_IFS=$IFS
IFS=$'\n'
FOLD=$1
FILE=`ls -t1 $FOLD | sort -r | head -n1`
SIZE=`stat -c %s $FOLD/$FILE`
let 'SIZE=SIZE / 1024 / 1024'
echo $SIZE
IFS=$OLD_IFS
