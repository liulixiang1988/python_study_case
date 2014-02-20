#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'liulixiang'

from bs4 import BeautifulSoup
import glob

left, left_times, left_weight = 0, 0, 0.0
right, right_times, right_weight = 0, 0, 0.0
files = sorted(glob.glob(r'E:\工作\work-documents\2013凤矿计量系统\Debug\WY.WeightBridge.Data\*.xml'))
for index, filename in enumerate(files, 1):
    file = open(filename, encoding='utf-8').read()
    soup = BeautifulSoup(file, 'xml')
    print(index,  '时间', soup.MeasureTime.string, '节数:', int(soup.NodeNumber.string), '方向:', soup.Orientation.string)
    for node in soup.FileBody.findChildren('Node'):
        print('\t序号:', node.ID.string, '重量:', node.Weight.string)
        if soup.Orientation.string == '左方向来车>>>>>>':
            left_weight += float(node.Weight.string)
        elif soup.Orientation.string == '右方向来车<<<<<<':
            right_weight += float(node.Weight.string)
    if soup.Orientation.string == '左方向来车>>>>>>':
        left += int(soup.NodeNumber.string)
        left_times += 1
    elif soup.Orientation.string == '右方向来车<<<<<<':
        right += int(soup.NodeNumber.string)
        right_times += 1
        print('\n')

print('左方向来车共{}次，共{}节，总皮重{:.2f}'.format(left_times, left, left_weight))
print('右方向来车共{}次，共{}节, 总毛重{:.2f}'.format(right_times, right, right_weight))
print('总净重：%.2f' % (right_weight - left_weight))
