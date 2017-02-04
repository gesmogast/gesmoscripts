#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import subprocess

col = 0
    # Проходимся по всем файлам в заданной папке
for i in os.listdir('/mnt/MDaemon/Inbound'):
	col += 1
print col
