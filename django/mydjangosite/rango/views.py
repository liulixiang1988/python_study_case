from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from .models import Category, Page


def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    for category in category_list:
        category.url = category.name.replace(' ', '_')
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return render(request, 'rango/about.html')


def category(request, category_name_url):
    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name': category_name}
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/cateogry.html', context_dict)

