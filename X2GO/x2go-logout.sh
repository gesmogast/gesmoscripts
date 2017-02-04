#! /bin/bash
echo -n "Enter username to disconnect:"
read username
let timeout=600
timeage=`sudo -u $username x2golistsessions |awk -F  "|" '{print $13}'`
#let timeage=`$operand`
if [ $timeage > $timeout ];then
    sessid=`sudo -u $username x2golistsessions |awk -F "|" '{print $2}'`
    x2goterminate-session $sessid
fi
echo "$username disconnected!"
sleep 3s
