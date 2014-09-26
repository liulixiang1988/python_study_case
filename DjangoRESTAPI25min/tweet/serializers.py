# -*- coding:utf-8 -*-
from tweet.models import Tweet

__author__ = 'liulixiang'

from rest_framework import serializers


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user')

    class Meta:
        model = Tweet
        fields = ('text', 'user', 'timestamp')


