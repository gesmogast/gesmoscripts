#! /bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    username=$line
    echo "$username logged out"
    let timeout=600
    timeage=`sudo -u $username x2golistsessions |awk -F  "|" '{print $13}'`
    if [ $timeage > $timeout ];then
        sessid=`sudo -u $username x2golistsessions |awk -F "|" '{print $2}'`
        x2goterminate-session $sessid
    fi
done < "/opt/users"
