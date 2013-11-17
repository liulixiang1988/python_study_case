#-*- coding:utf-8 -*-
import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('发布日期')

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text