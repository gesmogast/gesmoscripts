#!/bin/bash
SERVER=$1
h=$2
str2=$3
zabbix_get -s $SERVER -k "smarttest[-i,"$h"]" | grep -i "Serial Number" | awk '{print $NF}'
