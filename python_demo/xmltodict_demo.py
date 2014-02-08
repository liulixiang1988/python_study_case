#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liulixiang'
import xmltodict

doc = xmltodict.parse('''<?xml version="1.0"?>
<VehicleInfo has="测试">
  <FileHeader>
    <ScaleInfo>
      <SN>H00120030101081526</SN>
      <UserName>盛隆钢铁</UserName>
      <SUMWeight>0</SUMWeight>
    </ScaleInfo>
  </FileHeader>
  <FileBody>
    <Node>
      <ID>1</ID>
      <_DateTime>2003-1-1 8:14:25</_DateTime>
      <VehicleType />
      <VehicleCardID />
      <Speed>17.5</Speed>
      <Weight>3.12</Weight>
      <PIC1>_1.bmp</PIC1>
    </Node>
    <Node>
      <ID>2</ID>
      <_DateTime>2003-1-1 8:14:26</_DateTime>
      <VehicleType />
      <VehicleCardID />
      <Speed>15.8</Speed>
      <Weight>4.77</Weight>
      <PIC1>_1.bmp</PIC1>
    </Node>
  </FileBody>
</VehicleInfo>
''', encoding='utf-8')

print(doc['VehicleInfo']["@has"])
for node in doc['VehicleInfo']['FileBody']['Node']:
    print(node['ID'], node['Weight'], node['_DateTime'])

