#!/bin/bash
find /mnt/db_backup/* -type d -ctime +3 | xargs rm -rf
folder=`date +/mnt/db_backup/\%Y\%m\%d.\%H\%M\%S`
/usr/bin/innobackupex --user=root --password=password $folder --no-timestamp >> /dev/null
/usr/bin/innobackupex --apply-log $folder >> /dev/null
