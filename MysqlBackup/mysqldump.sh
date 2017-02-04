#!/bin/bash
rm -rf /mnt/backup_db/*
/usr/bin/mysqldump -u root -p'password' database --ignore-table=database.history_uint --ignore-table=database.history --ignore-table=database.history_text >> `date +/mnt/backup_db/dump.\%Y\%m\%d.\%H\%M\%S.sql`
