#!/usr/bin/env python
import ssl
from pysphere import *
from pysphere.vi_virtual_machine import VIVirtualMachine

default_context = ssl._create_default_https_context
server = VIServer()
try:
    ssl._create_default_https_context = ssl._create_unverified_context
    server.connect("ip", "administrator@vsphere.local", "password")
    vms = server.get_registered_vms()
    for i in vms:
        print i
#     for config in vm.properties.config.hardware.device:
#        print config.key, "=>", config.value  
finally:
    ssl._create_default_https_context = default_context
