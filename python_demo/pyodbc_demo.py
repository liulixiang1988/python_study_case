#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pyodbc

# DRIVER在本机和目标机器上必须一致，比如本机是2008数据库，目标机器也必须是2008数据库，否则会出错
cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=testdb;UID=sa;PWD=123456')
cursor = cnxn.cursor()

cursor.execute("select user_name, password from users")
row = cursor.fetchone()
if row:
    print(row)

cursor.execute("insert into users(user_name, password, nick_name) values(?, ?, ?)", "liulixiang1988", "123", "刘理想")
cnxn.commit()

# query multiple lines
cursor.execute("select * from users")
for row in cursor:
    print(row.id, row.user_name, row.password, row.nick_name)
# or:
# rows = cursor.fetchall()
# for row in rows:
#     print(...)


cursor.close()
cnxn.close()
