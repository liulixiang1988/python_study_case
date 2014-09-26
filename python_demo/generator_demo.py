#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liulixiang'

import os


def tree(top):
    for path, dirnames, fnames in os.walk(top):
        for fname in fnames:
            yield os.path.join(path, fname)


for name in tree(os.path.dirname(__file__)):
    print(name)

