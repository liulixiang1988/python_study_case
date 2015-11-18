#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

r = urllib2.urlopen("http://z.cn")
html = r.read()
print(html)
