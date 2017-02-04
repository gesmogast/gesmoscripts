#!/bin/bash
COMM=`sed -n $1 '/home/ebro/ebro_output.txt' | head -n1 | awk '{print $1;}' | tr -d 'ºC%' | tr ',' '.'`
echo $COMM
