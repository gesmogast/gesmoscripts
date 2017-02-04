#!/usr/bin/env python
# vSphere report to obtain information about existing snapshots on VM's
#
import ssl
from pysphere import *
from pysphere.vi_virtual_machine import VIVirtualMachine

default_context = ssl._create_default_https_context
server = VIServer()
try:
    ssl._create_default_https_context = ssl._create_unverified_context
    server.connect("ip", "administrator@vsphere.local", "password")
    vms = server.get_registered_vms(status="poweredOn")
    for vm in vms:
        virtual_machine = server.get_vm_by_path(vm)
        snapshots = virtual_machine.get_snapshots()
	if snapshots != []:
            print virtual_machine.get_property('name'), virtual_machine.get_property('ip_address'), virtual_machine.get_property('guest_full_name') 
	    print "SNAPSHOT FOUND"
            print "*****************************************" 
finally:
    ssl._create_default_https_context = default_context
