# -*- coding:utf-8 -*-

from django.contrib import admin
__author__ = 'Liu Lixiang'

from books.models import *

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class ShelfAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Shelf, ShelfAdmin)