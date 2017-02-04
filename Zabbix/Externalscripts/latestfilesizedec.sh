#!/bin/bash
FOLD=$1
DISK=$2
FILE=`ls -t1 $FOLD | sort -r | head -n4 | grep $DISK | tail -n 1`
SIZE=`stat -c %s $FOLD/$FILE`
let 'SIZE=SIZE / 1024 / 1024'
echo $SIZE
