# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('文章分类', max_length=120)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'
        ordering = ['-id', ]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('标题', max_length=120)
    author = models.ForeignKey(User)
    content = models.TextField('内容')
    po_type = models.ForeignKey(Category, verbose_name='文章分类', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-id']

    def __str__(self):
        return self.title

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('post', (), {'pk': self.pk})
