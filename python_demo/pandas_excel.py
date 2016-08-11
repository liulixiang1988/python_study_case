# -*- coding:utf-8 -*-

import pandas

ds = pandas.read_excel('识别结果_25.xlsx', skiprows=2)
ds['识别结果'] = ds['识别结果'].str.replace(r'{/*p\d*}', '')
writer = pandas.ExcelWriter('识别结果_25_2.xlsx', engine='xlsxwriter')
ds.to_excel(writer)
writer.save()
