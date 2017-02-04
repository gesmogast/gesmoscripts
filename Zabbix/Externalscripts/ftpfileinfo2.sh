#!/bin/bash
#Количество часов с момента записи в файл по сравнению с текущим временем
FOLDER=$1
echo -n > /usr/lib/zabbix/externalscripts/tmpftpinfo.txt
cp /dev/null tmpftpinfo.txt
export TMPRESULT=0
cd $FOLDER
ls *.txt | while read FILENAME; do
	TMP=$FOLDER"$FILENAME"
	#echo $TMP
	#echo `cat $TMP`
	#echo `cat $TMP | sed -n '1p' | tr "." "-"`
	#echo '******'
	arr[0]=$(cat $TMP | sed -n '1p' | tr "." "-")
	#echo ${arr[0]}
	a1=${arr[0]:6:4}
	a2=${arr[0]:3:2}
	a3=${arr[0]::2}
	a123=$a1
	a123+="-"
	a123+=$a2
	a123+="-"
	a123+=$a3
	F1=`cat $TMP | sed -n '2p'`
	a123+=" "
	a123+=$F1
	result1=$(date -d "$a123" +%s)
	result2=$(date +%s)
	export diffresult=$(((result2-result1)/3600))
if [ $diffresult -le 700 ]
then
	if [ $diffresult -ge 10 ]
	then
	#echo $diffresult
	let TMPRESULT+=1
	fi
fi
	echo $TMPRESULT >> /usr/lib/zabbix/externalscripts/tmpftpinfo.txt
done
final=`tail -n 1 /usr/lib/zabbix/externalscripts/tmpftpinfo.txt | head -n 1`
echo $final
