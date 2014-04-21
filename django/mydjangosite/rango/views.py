from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from .models import Category


def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return render(request, 'rango/about.html')
