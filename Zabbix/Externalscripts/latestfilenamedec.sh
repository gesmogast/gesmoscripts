#!/bin/bash
FOLD=$1
DISKNAME=$2
FILE=`ls -t1 $FOLD | sort -r | head -n5 | grep $DISKNAME | tail -n 1`
echo $FILE
