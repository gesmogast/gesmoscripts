#!/bin/bash
SERVER=$1
h=$2
str=$3
zabbix_get -s $SERVER -k "smarttest[-H,"$h"]" | grep -i $str | awk '{print $NF}'
