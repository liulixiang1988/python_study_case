# -*- coding:utf-8 -*-
from rest_framework.response import Response
from rest_framework.decorators import api_view

from books.serializers import *


@api_view(['GET'])
def all_books(request, **kwargs):
    books = Book.objects.all()
    serializers = BookSerializer(books, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def add_book(request, **kwargs):
    title = request.data['title']
    if 'desc' in request.data:
        desc = request.data['desc']
    else:
        desc = ''
    book = Book.objects.create(
        title=title,
        desc=desc)
    serializer = BookSerializer(book)
    return Response(serializer)


@api_view(['POST'])
def add_author(request, **kwargs):
    author = Author.objects.get(pk=request.data['author_pk'])
    book = Book.objects.get(pk=request.data['book_pk'])

    if author not in book.authors.all():
        book.authors.add(author)
        book.save()

    serializer = BookSerializer(book)
    return Response(serializer.data)
