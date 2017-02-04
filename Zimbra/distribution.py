#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Covert MDaemon exported users from .csv to Zimbra commands
# creating distribution lists and adding members
# import command
# just execute python3 script

import os

#remove first line from csv file (contains no needed header)
os.system("sed -i '1d' users.csv")
distlistname = input("Enter distribution list name: ")
print("Creating distribution list",distlistname)
# execute command to create distribution list in Zimbra
command = "zmprov cdl "+distlistname+"@maildomain"
os.system(command)
# convert users.csv mdaemon file to Zimbra-friendly tmp file
morphcommand = "grep -r \"maildomain\" users.csv | cut -d \",\" -f1 | sed 's/\"//g' | tr A-Z a-z | sort > morphdist.tmp"
# execute command to convert .csv
os.system(morphcommand)
# execute import
with open('morphdist.tmp', 'rU') as csvfile:
    for line in csvfile:
        diststr = "zmprov adlm "+distlistname+"@aildomain "+line 
        print("Import "+line)
        os.system(diststr)
