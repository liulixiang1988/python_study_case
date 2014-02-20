#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ftplib import FTP

ftp = FTP('172.16.8.36', 'rjb', 'rjb5860247')
print(ftp.dir())