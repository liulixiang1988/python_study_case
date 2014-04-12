from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse


def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': '消息在这儿'}
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return render(request, 'rango/about.html')
