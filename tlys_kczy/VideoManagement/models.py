# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class VideoCategory(models.Model):
    category_name = models.CharField('视频类别', max_length=200)

    class Meta:
        verbose_name = '视频类别'
        verbose_name_plural = '视频类别'

    def __str__(self):
        return self.category_name


class Videos(models.Model):
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
        VideoCategory,
        verbose_name='视频类别',
        blank=True)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = '视频'

    def __str__(self):
        return self.title
