#!/bin/bash
#Количество часов с момента записи в файл по сравнению с текущим временем
FOLD=$1
arr[0]=$(cat $FOLD | sed -n '1p' | tr "." "-")
a1=${arr[0]:6:4}
a2=${arr[0]:3:2}
a3=${arr[0]::2}
a123=$a1
a123+="-"
a123+=$a2
a123+="-"
a123+=$a3
F1=`cat $FOLD | sed -n '2p'`
a123+=" "
a123+=$F1
result1=$(date -d "$a123" +%s)
result2=$(date +%s)
diffresult=$(((result2-result1)/3600))
echo $diffresult

