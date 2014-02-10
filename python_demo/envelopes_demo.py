#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liulixiang'

from envelopes import Envelope,SMTP, GMailSMTP

#构造envelop
envelope = Envelope(
    from_addr=('test1@qq.com', '理想'),
    to_addr=('test2@qq.com', '刘理想'),
    subject='envelope库的使用',
    text_body='envelope是一个python库，可以用来发送邮件'
)
#添加附件
envelope.add_attachment('/Users/liulixiang/Downloads/1.png')

#发送邮件
#发送邮件方法1
envelope.send('smtp.qq.com', login='test1@qq.com', password='123')

#发送邮件方法2
qq = SMTP(host='smtp.qq.com', login='test2@qq.com', password='123')
qq.send(envelope)

