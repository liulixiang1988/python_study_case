#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ftplib import FTP

ftp = FTP('172.16.216.31', 'rydw', '5860666')
print(ftp.dir())