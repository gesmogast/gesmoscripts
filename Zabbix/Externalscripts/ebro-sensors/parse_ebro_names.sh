#!/bin/bash
COMM=`sed -n $1 '/home/ebro/ebro_output.txt' | head -n1 | awk '{print $2,$3,$4,$5;}'`
echo $COMM
