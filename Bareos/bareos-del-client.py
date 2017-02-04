#!/usr/bin/python
import os
choice = raw_input("Enter delete option (1 - delete host client, 2 - delete vm client): ")
# Procedure for host system backup
def delete_host():
	print('Host system client deletion')
	print('Enter client name (like srv-test-server-fd)')
	del_client_name = raw_input("Client name: ")
	client_filename = "/etc/bareos/conf.d/hosts/"+del_client_name+".conf"
	with open(client_filename,'r') as clientsfile:
		lines = clientsfile.readlines()
		for i in lines:
			print i

# Procedure for backup of virtual machines
def delete_vm():
	print('VM client deletion')
	print('Enter vm name (like srv-test-server-vm)')
	del_client_name = raw_input("Enter vm name (as it is in vSphere): ")
		# Add vm client configuration to vsphre host file
	client_filename = "/etc/bareos/conf.d/vsphere/"+del_client_name+".conf"
	with open(client_filename,'w+') as clientsfile:
		clientsfile.write(template_job)
		clientsfile.write(template_fileset)
		clientsfile.write(template_storage)
		clientsfile.write(template_pool)
	
if choice == '1':
	delete_host()
elif choice == '2':
	delete_vm()
else:
	print("Wrong number! Exit.")