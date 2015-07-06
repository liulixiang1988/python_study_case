# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from books.serializers import *

@api_view(['GET'])
def all_books(resquest, **kwargs):
    books = Book.objects.all()
    serializers = BookSerializer(books, many=True)
    return Response(serializers.data)
