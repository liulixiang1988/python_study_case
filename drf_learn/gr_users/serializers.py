# -*- coding:utf-8 -*-
__author__ = 'Liu Lixiang'
from django.contrib.auth.models import User
from rest_framework import serializers
from gr_users.models import GRUser
from books.serializers import ShelfSerializer, BookSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username')


class GRUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    shelves = ShelfSerializer(many=True)
    books = BookSerializer(many=True)

    class Meta:
        model = GRUser
        fields = ('pk', 'user', 'first_name', 'last_name', 'shelves', 'books')
