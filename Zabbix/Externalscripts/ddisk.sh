#!/bin/bash

SRV=$1
n=0


for i in `zabbix_get -s $SRV -k 'smart.discovery' | awk '{print $1}'`
do
  if [ `zabbix_get -s $SRV -k "smarttest[-A,\"$i\"]" |  sed 1,7d | wc -l` -gt 0 ]
   then
    n=$[$n+1]
     h[$n]=$i
   fi
done

if [ -z ${h[1]} ]
    then
    echo "smart not supported"
    else
i=1
j=$[$n-1]
echo "{ \"data\":
["
    while [ $i -le $j ]
    do
    echo "{ \"{#HDD}\":\"${h[$i]}\" } ,"
    i=$[$i+1]
    done
echo "{ \"{#HDD}\":\"${h[$i]}\" } "
echo " ] } "
fi