#-*- coding:utf-8 -*-
import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
class Poll(models.Model):
    question = models.CharField('投票', max_length=200)
    #pub_date = models.DateTimeField('发布日期', auto_now_add=True)
    pub_date = models.DateTimeField('发布日期', default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布'

    class Meta:
        verbose_name = '投票'
        verbose_name_plural = '投票'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField('选择', max_length=200)
    votes = models.IntegerField('票数', default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = '选择'
        verbose_name_plural = '选择'
