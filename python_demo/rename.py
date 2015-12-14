#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from os import path
files = []

for(dirpath, dirnames, filenames)in os.walk("."):
    files = filenames

files = [(os.path.split(file)[-1], path.getmtime(file)) for file in files]
files.sort(key=lambda x: x[1])
print(files)
ignore = os.path.split(__file__)[-1]
for i, (file, _) in enumerate(files):
    if file == ignore:
        continue
    os.rename(file, "%2d-%s" % (i, file))
