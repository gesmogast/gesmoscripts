#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import subprocess
import datetime
path = '/mnt/MailLock/'
temp = 0
for file in os.listdir(path):
	statinfo = os.stat(path+file)
	timestamp = statinfo.st_mtime
	maximum_timestamp = time.time() - timestamp
	# Exists lock file for more than 5 minutes
	if (600 > maximum_timestamp > 300):
		temp = 1
	# Exists lock file for more than 10 minutes, deleting it
	if maximum_timestamp > 600:
		#os.remove(path+file)
		os.remove(path+file)
		temp = 0
	#print maximum_timestamp
print temp


