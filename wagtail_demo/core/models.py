# -*- coding:utf-8 -*-
from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):

    body = RichTextField('内容', blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

    class Meta:
        verbose_name = '首页'
        verbose_name_plural = '首页'

    def __str__(self):
        return '首页'
