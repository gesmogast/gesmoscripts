#!/usr/bin/python
import os
choice = raw_input("Enter backup option (1 - host system, 2 - vm backup): ")
# Procedure for host system backup
def backup_host():
	print('Host system backup')
	print('Adding client information to backup system')
	backup_client_name = raw_input("Enter system name: ")
	backup_client_name += '-fd'
	backup_client_ip = raw_input("Enter system ip address: ")
	backup_client_label = raw_input("Enter backup client label format (like Graylog, Unifi): ")
	schedule_format = """Backup schedule format:
  at 09:00 - backup every day at 9:00
  sun at 13:00 - backup every sunday at 13:00
  fri at 15:00 - backup every friday at 15:00
  etc..
	"""
	print(schedule_format)
	backup_client_schedule = raw_input("Enter backup schedule: ")
	# Add clients configuration
	template_client = """Client {
  Name = %s
  Password = quakequake
  Address = %s
  FDPort = 9102
  Catalog = MyCatalog
  File Retention = 30 days
  Job Retention = 30 days
}
	""" % (backup_client_name, backup_client_ip)
	# Add jobs configuration
	template_job = """Job {
  Name = "Backup %s"
  Type = Backup
  Level = Full
  Client = %s
  FileSet = "System"
  Schedule = Backup%s
  Storage = %s
  Pool = Backup%s
  Spool Data = no
  Spool Attributes = yes
  Messages = Standard
}
	""" % (backup_client_label,backup_client_name,backup_client_label,backup_client_label,backup_client_label)
	# Add storages configuration
	template_storage = """Storage {
  Name = %s
  Address = 10.12.1.111
  SDPort = 9103
  Password = quakequake
  Device = Backup%s
  Media Type = File
  Maximum Concurrent Jobs = 1
}
	""" % (backup_client_label,backup_client_label)
	# Add pools configuration
	template_pool = """Pool {
  Name = Backup%s
  Pool Type = Backup
  Maximum Volume Jobs = 1
  Volume Retention = 30 days
  Recycle = yes
  AutoPrune = yes
  Purge Oldest Volume = yes
  LabelFormat = %s-Backup-
  Maximum Volumes = 4
  Maximum Volume Bytes = 500G
}
	""" % (backup_client_label,backup_client_label)
	client_filename = "/etc/bareos/conf.d/hosts/"+backup_client_name+".conf"
	with open(client_filename,'w+') as clientsfile:
		clientsfile.write(template_client)
		clientsfile.write(template_job)
		clientsfile.write(template_storage)
		clientsfile.write(template_pool)
	print('Client configuration added!')
	# Add devices configuration
	template_device = """Device {
  Name = Backup%s
  Archive Device = /mnt/backup/%s
  Media Type = File
  LabelMedia = yes
  Random Access = yes
  AutomaticMount = yes
  RemovableMedia = no
  AlwaysOpen = no
}
	""" % (backup_client_label,backup_client_label)
	with open('/etc/bareos/conf.d/devices.conf','a') as devicesfile:
		devicesfile.write(template_device)
	print('Device configuration added!')
	dir_name = "/etc/bareos/bareos-dir.conf"
	template_dir = "@/etc/bareos/conf.d/hosts/%s.conf\n" % (backup_client_name)
	with open(dir_name,'a') as dirname:
		dirname.write(template_dir)

	# Add schedules configuration
	template_schedule = """Schedule {
  Name = Backup%s
  Run = Level=Full %s
}
	""" % (backup_client_label,backup_client_schedule)
	with open('/etc/bareos/conf.d/schedules.conf','a') as schedulefile:
		schedulefile.write(template_schedule)
	print('Schedule configuration added!')

	# Create backup folders and restart daemons
	print('Grant bareos permissions over host configuration file')
	os.system("chown bareos:bareos %s" % client_filename)

	print('Creating backup folder /mnt/backup/%s' % backup_client_label)
	backup_string = "mkdir -p /mnt/backup/%s >> /dev/null" % (backup_client_label)
	os.system(backup_string)
	print('Backup folder created!')
	print('Restarting bareos daemons...')
	os.system("service bareos-dir restart > /dev/null")
	os.system("service bareos-sd restart > /dev/null")
	print('Bareos daemons restarted!')

# Procedure for backup of virtual machines
def backup_vm():
	print('VM Backup')
	print('Adding client information to backup system')
	backup_client_name = raw_input("Enter vm name (as it is in vSphere): ")
	schedule_format = """Backup schedule format:
  at 09:00 - backup every day at 9:00
  sun at 13:00 - backup every sunday at 13:00
  fri at 15:00 - backup every friday at 15:00
  etc..
	"""
	print(schedule_format)
	backup_client_schedule = raw_input("Enter backup schedule: ")
	template_job = """Job {
  Name = "vm-%s"
  FileSet = "vm-%s-fileset"
  Type = Backup
  Level = Full
  Client = srv-backup-02-fd
  Schedule = Backup-%s
  Storage = Backup%s
  Pool = Backup%s
  Messages = Standard
}
	""" % (backup_client_name,backup_client_name,backup_client_name,backup_client_name,backup_client_name)
	template_fileset = """FileSet {
  Name = "vm-%s-fileset"
  Include {
	Options {
		signature = MD5
	}
	Plugin = "python:module_path=/usr/lib/bareos/plugins/vmware_plugin:module_name=bareos-fd-vmware:dc=IFX-DC:folder=/:vmname=%s:vcserver=srv-vcenter-01.interfarmax.local:vcuser=bareos:vcpass=IFXnet314bac!"
  }
}
	""" % (backup_client_name,backup_client_name)
	template_storage= """Storage {
  Name = Backup%s
  Address = <director ip>
  SDPort = 9103
  Password = quakequake
  Device = Backup%s
  Media Type = File
  Maximum Concurrent Jobs = 1
}
	""" % (backup_client_name,backup_client_name)
	template_pool= """Pool {
  Name = Backup%s
  Pool Type = Backup
  Maximum Volume Jobs = 1
  Volume Retention = 30 days
  Recycle = yes
  AutoPrune = yes
  LabelFormat = %s-Backup-
  Maximum Volumes = 4
  Maximum Volume Bytes = 500G
}
	""" % (backup_client_name,backup_client_name)
	template_device= """Device {
  Name = Backup%s
  Archive Device = /mnt/backup/vSphere/%s
  Media Type = File
  LabelMedia = yes
  Random Access = yes
  AutomaticMount = yes
  RemovableMedia = no
  AlwaysOpen = no
}
	""" % (backup_client_name,backup_client_name)
	# Add vm client configuration to vsphre host file
	client_filename = "/etc/bareos/conf.d/vsphere/"+backup_client_name+".conf"
	with open(client_filename,'w+') as clientsfile:
		clientsfile.write(template_job)
		clientsfile.write(template_fileset)
		clientsfile.write(template_storage)
		clientsfile.write(template_pool)
	print('Client configuration added!')
	dir_name = "/etc/bareos/bareos-dir.conf"
	template_dir = "@%s\n" % (client_filename)
	with open(dir_name,'a') as dirname:
		dirname.write(template_dir)
	with open('/etc/bareos/conf.d/devices.conf','a') as devicesfile:
		devicesfile.write(template_device)
	print('Device configuration added!')

        # Add schedules configuration
        template_schedule = """Schedule {
  Name = Backup-%s
  Run = Level=Full %s
}
        """ % (backup_client_name,backup_client_schedule)
        with open('/etc/bareos/conf.d/schedules.conf','a') as schedulefile:
                schedulefile.write(template_schedule)
        print('Schedule configuration added!')

	# Create backup folders and restart daemons
	print('Grant bareos permissions over host configuration file')
	os.system("chown bareos:bareos %s" % client_filename)

	print('Creating backup folder /mnt/backup/vSphere/%s' % backup_client_name)
	backup_string = "mkdir -p /mnt/backup/vSphere/%s >> /dev/null" % (backup_client_name)
	os.system(backup_string)
	print('Backup folder created!')
	print('Enabling CBT for VM')
	# Running system command to enable CBT on virtual machine
	os.system("vmware_cbt_tool.py -s <vcenter-name> -u administrator@vsphere.local -p <password> -d <DC> -f / -v %s --enablecbt >> /dev/null" % backup_client_name)
	print('CBT for VM enabled!')
	print('Restarting bareos daemons...')
	os.system("service bareos-dir restart > /dev/null")
	os.system("service bareos-sd restart > /dev/null")
	print('Bareos daemons restarted!')
if choice == '1':
	backup_host()
elif choice == '2':
	backup_vm()
else:
	print("Wrong number! Exit.")