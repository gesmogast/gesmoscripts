#!/bin/bash
export PATH=${PATH}:/usr/local/sbin:/sbin:/usr/sbin:/bin:/usr/bin
[ -z "${1}" ] && exit
FOLDER="`echo "$1" | sed 's/\/$//'`"
if [ -d "${1}" ] ; then
  FILE="`ls -1pt "${FOLDER}/" | grep -v '/$' | head -n1`"
  STAMP=0
  if [ ! -z "${FILE}" ] ; then
    STAMP=`stat -c%Z "${FOLDER}/${FILE}" | awk -F\. '{print $1}'`
  fi
  echo "`date +%s` ${STAMP}" | awk '{print $1 - $2}'
fi