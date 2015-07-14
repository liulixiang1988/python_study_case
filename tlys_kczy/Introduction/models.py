# -*- coding:utf-8 -*-
from django.db import models

from DjangoUeditor.models import UEditorField


class Introduction(models.Model):
    title = models.CharField('标题',
                             max_length=200,
                             default='安徽铜陵矽卡岩型铜多金属矿基地建设简介')

    content = UEditorField(
        '内容',
        width=600,
        height=800,
        toolbars='full',
        imagePath='images/%(basename)s_%(datetime)s.%(extname)s',
        filePath='files/%(basename)s_%(datetime)s.%(extname)s')
    create_date = models.DateTimeField(
        '创建时间', auto_now_add=True, null=True)
    last_update_date = models.DateTimeField(
        '最后更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = "基本介绍"
        verbose_name_plural = "基本介绍"

    def __str__(self):
        return self.title
