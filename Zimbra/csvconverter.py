#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Covert MDaemon exported users from .csv to Zimbra zmprov file
# import command
# copy users.csv file to the same folder and run as user zimbra ./csvconverter.py

import csv
import os

i = 0
email = []
username = []
name = []
password = []

# open users.csv file and add data to lists - email username name
with open('users.csv') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='"')
# creating lists with user data
    for row in filereader:
        email.append(row[0])
        username.append(row[1])
        name.append(row[3])
        password.append(row[5])

print("cd dns-name2")
# iterate elements in list and create 'create account' records
for i in range(0,len(name)-1):
    # if password less than 6 symbols then create new one (otherwise change password policy)
    if len(password[i]) < 6:
        password[i] = "abc"+username[i][0:4] 
    # split username and surname
    gn = name[i].split()
    # deal with records, where more than 2 words in surname\name
    if len(gn) >= 2:
        castring = "zmprov createAccount "+email[i].replace("dns-name1","dns-name2")+" "+password[i]+" displayName "+"'"+gn[0]+" "+gn[1]+"'"+" givenName "+"'"+gn[1]+"'"+" sn "+"'"+gn[0]+"'"
        print("Importing "+email[i])
        os.system(castring)
    else:
        castring = "zmprov createAccount "+email[i].replace("dns-name1","dns-name2")+" "+password[i]+" displayName "+"'"+gn[0]+"'"+" givenName "+"'"+gn[0]+"'"+" sn "+"'"+gn[0]+"'"
        print("Importing "+email[i])
        os.system(castring)
