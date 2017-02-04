#!/bin/bash
SERVER=$1
h=$2
str=$3
zabbix_get -s $SERVER -k "smarttest[-i,"$h"]" 2>&1 | grep $str | awk '{print $NF}'
