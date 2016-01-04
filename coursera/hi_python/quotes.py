# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:41:02 2016

@author: Liu Lixiang
"""

from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date, datetime
import pandas as pd

today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('AXP', start, today)
fields = ['date', 'open', 'close', 'high', 'low', 'volume']
list1 = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0])) #转化为常规时间
    y = datetime.strftime(x, '%Y-%m-%d') #转换为固定格式
    list1.append(y)
#给DataFrame添加name属性
df = pd.DataFrame(quotes, index=list1, columns=fields)
#删除原有date列
df = df.drop(['date'], axis=1)
print(df)

#数据选择
print(df['2015-12-01':'2015-12-07'])

import time
listitem=[]
for i in range(0, len(df)):
    temp = time.strptime(df.index[i], '%Y-%m-%d')
    listitem.append(temp.tm_mon)
print(listitem)
tempdf = df.copy()
tempdf['month'] = listitem
print(tempdf)
print(tempdf.groupby('month').count())
print(tempdf.groupby('month').sum().volume)