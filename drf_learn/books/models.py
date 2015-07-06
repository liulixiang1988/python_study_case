# -*- coding:utf-8 -*-
from django.db import models

class Author(models.Model):
    first_name = models.CharField('姓', max_length=100)
    last_name = models.CharField('名', max_length=100)
    display_name = models.CharField('显示名', max_length=100, blank=True)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    title = models.CharField('书名', max_length=100)
    desc = models.TextField('描述', max_length=2500, blank=True)
    authors = models.ManyToManyField(Author, blank=True)

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = '图书'

    def __str__(self):
        return self.title


class Shelf(models.Model):
    title = models.CharField('书架名', max_length=100)
    books = models.ManyToManyField(Book, blank=True)

    class Meta:
        verbose_name = '书架'
        verbose_name_plural = '书架'

    def __str__(self):
        return self.title
