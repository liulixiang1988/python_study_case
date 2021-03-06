# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class ImageCategory(models.Model):
    category_name = models.CharField('图片类别', max_length=200)

    class Meta:
        verbose_name = '图片类别'
        verbose_name_plural = '图片类别'

    def __str__(self):
        return self.category_name


class Images(models.Model):
    title = models.CharField('标题', max_length=200)
    create_date = models.DateTimeField(
        '创建时间', auto_now_add=True, null=True)
    last_update_date = models.DateTimeField(
        '最后更新时间', auto_now=True, null=True)
    author = models.ForeignKey(User, verbose_name='作者')
    content = UEditorField(
        '内容',
        width=600,
        height=800,
        toolbars='full',
        imagePath='images/%(basename)s_%(datetime)s.%(extname)s',
        filePath='files/%(basename)s_%(datetime)s.%(extname)s')
    categorys = models.ManyToManyField(
        ImageCategory,
        verbose_name='图片类别',
        blank=True)

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'

    def __str__(self):
        return self.title
