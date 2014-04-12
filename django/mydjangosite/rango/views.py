from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, Rango, <a href="/rango/about/">关于</a>')


def about(request):
    return HttpResponse('这是关于页面')
