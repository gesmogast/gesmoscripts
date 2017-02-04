#! /bin/bash
echo "Logged in X2GO users:"
while IFS='' read -r line || [[ -n "$line" ]]; do
    username=$line
    let timeout=600
    timeage=`sudo -u $username x2golistsessions |awk -F  "|" '{print $12}'`
    if [ "$timeage" != '' ]
    then ipaddress=`sudo -u $username x2golistsessions |awk -F  "|" '{print $8}'`
         echo "$timeage from $ipaddress"
         echo "*****"
    fi
    timeage=''
done < "/opt/users"
read -p "Press any key to continue... " -n1 -s

