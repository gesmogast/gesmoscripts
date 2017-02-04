#!/usr/bin/env python
# vSphere report to obtain information about running VM's
# Output format:
# - VM Name
# - ESXi Host
# - VM Datastore
# - VM CPU
# - VM Memory
# - VM Disks
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
	print "SYSTEM: ",virtual_machine.get_property('name'), virtual_machine.get_property('ip_address'), virtual_machine.get_property('guest_full_name')
        print "HOST: ",virtual_machine.properties.runtime.host.name
        print "DATASTORE: ", vm
        print "CPU: ",virtual_machine.properties.config.hardware.numCPU,
        print "MEMORY: ",virtual_machine.properties.config.hardware.memoryMB,"MB"
        print "DISKS"
        disks = [d for d in virtual_machine.properties.config.hardware.device
            if d._type=='VirtualDisk'
            and d.backing._type in ['VirtualDiskFlatVer1BackingInfo',
                                 'VirtualDiskFlatVer2BackingInfo',
                                 'VirtualDiskRawDiskMappingVer1BackingInfo',
                                 'VirtualDiskSparseVer1BackingInfo',
                                 'VirtualDiskSparseVer2BackingInfo'
                                 ]]
        for disk in disks:
            print "Label: ", disk.deviceInfo.label
            print "Summary: ", disk.deviceInfo.summary
            print "File: ", disk.backing.fileName
            if hasattr(disk.backing, "thinProvisioned"):
                print "Thin provisioned:", disk.backing.thinProvisioned
            print "______________________"
        snapshots = virtual_machine.get_snapshots()
        if snapshots == []: print "SNAPSHOTS: None"
	else: print "SNAPSHOTS: Yes"
        print "*****************************************" 
finally:
    ssl._create_default_https_context = default_context
