#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
编程小练习（不计分）
~~~

创建一个文件src.txt，文件内容为：
How many seas must a white dove sail
Before she sleeps in the sand

将src.txt的内容复制到文件dest.txt中，并在dest.txt文件头部添加另两行字符串，添加后dest.txt文件中的内容为：

How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand

'''

src = open('src.txt', 'w+')
src.write('How many seas must a white dove sail\n')
src.write('Before she sleeps in the sand\n')
src.close()

src = open('src.txt', 'r+')
lines = src.readlines()
lines.insert(0, 'How many roads must a man walk down\n')
lines.insert(1, 'Before they call him a man\n')
dest = open('dest.txt', 'w+')
dest.writelines(lines)
dest.close()
