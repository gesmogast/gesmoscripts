#!/bin/bash
FILE=$1
OPTION=$2
COMM=`sed -n $OPTION'p' $FILE`
echo $COMM

