# -*- coding:utf-8 -*-

from django.db import models

from django.contrib.auth.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
