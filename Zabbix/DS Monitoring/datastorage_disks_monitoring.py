#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import subprocess

#Функция поиска здоровья диска
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return "ERROR"
        
module = 100
i = -1
health = 'display-name="Health">'
ender = '</PROPERTY>'
model = 'display-name="Model">'
serial = 'display-name="Serial Number">'
ident = 'display-name="Durable ID">'
ABS_PATH="/home/hpstorage/output"
#try: 
	#print ABS_PATH+'/perl_out.txt'
#	f = open(ABS_PATH+'/Disks/perl_out.txt','r')
#except IOError:
#	print ("No File")
#Выходной файл - output - значение минимума
output_health = open(ABS_PATH+'/Disks/health.txt','w')
output_model = open(ABS_PATH+'/Disks/model.txt','w')
output_serial = open(ABS_PATH+'/Disks/serial.txt','w')
output_ident = open(ABS_PATH+'/Disks/ident.txt','w')
output_enclosures = open(ABS_PATH+'/Enclosures/enclosures.txt','w')
#output_debug = open(ABS_PATH+'/Disks/debug.txt','w')
#Выходной файл - output - значение максимума
#output_disk1_2 = open(ABS_PATH+'\disk_1.2\health.txt','w')
#Чтение всего файла в строку, сканирование всего файла по смещениям

#Здоровье дисков
f = open(ABS_PATH+'/perl_out.txt','r')
s = f.readline()
while s:
	i += 1
	if i >= 138:
		module = (i - 72) % 67
	if (i == 72) or (module == 0):
		#output_debug.write(str(i) + ' - ' + s + '\n')
		output_health.write(find_between(s, health, ender)+'\n')	
	s = f.readline()
	if i >= 1614:
		break

#Модель дисков
output_health.close()
f.close()
f = open(ABS_PATH+'/perl_out.txt','r')
i = -1
module = 100
s = f.readline()
while s:
	i += 1
	if i >= 87:
		module = (i - 20) % 67
	if (i == 20) or (module == 0):
		output_model.write(find_between(s, model, ender)+'\n')	
	s = f.readline()
	if i == 1627:
		break

#Серийный номер
f.close()
f = open(ABS_PATH+'/perl_out.txt','r')
i = -1
module = 100
s = f.readline()
while s:
	i += 1
	if i >= 85:
		module = (i - 18) % 67
	if (i == 18) or (module == 0):
		output_serial.write(find_between(s, serial, ender)+'\n')	
	s = f.readline()
	if i == 1560:
		break

#Идентификатор
f.close()
f = open(ABS_PATH+'/perl_out.txt','r')
i = -1
module = 100
s = f.readline()
while s:
	i += 1
	if i >= 78:
		module = (i - 11) % 67
	if (i == 11) or (module == 0):
		output_ident.write(find_between(s, ident, ender)+'\n')	
	s = f.readline()
	if i == 1560:
		break
f.close()

#Получение информации о шасси (БП, Контроллеры и др.)
f = open(ABS_PATH+'/Enclosures/hp_datastore_enc.txt','r')
i = -1
module = 100
s = f.readline()
while s:
        i += 1
	#Enclosure Info
        if i == 57:
                output_enclosures.write(find_between(s, health, ender)+'\n')
        if i == 641:
                output_enclosures.write(find_between(s, health, ender)+'\n')
	#Controllers Info
        if i == 105:
                output_enclosures.write(find_between(s, health, ender)+'\n')
	if i == 321:
                output_enclosures.write(find_between(s, health, ender)+'\n')
	#Enclosure 2 IOModule
        if i == 667:
                output_enclosures.write(find_between(s, health, ender)+'\n')
        if i == 722:
                output_enclosures.write(find_between(s, health, ender)+'\n')
	#PSU Enclosure 1 and 2
        if i == 519:
                output_enclosures.write(find_between(s, health, ender)+'\n')
        if i == 569:
                output_enclosures.write(find_between(s, health, ender)+'\n')
        if i == 781:
                output_enclosures.write(find_between(s, health, ender)+'\n')
        if i == 831:
                output_enclosures.write(find_between(s, health, ender)+'\n')
        #CF Controller A and B
        if i == 271:
                output_enclosures.write(find_between(s, health, ender)+'\n')
        if i == 487:
                output_enclosures.write(find_between(s, health, ender)+'\n')
      	s = f.readline()
        if i == 850:
                break

