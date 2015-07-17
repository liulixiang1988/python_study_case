# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator
from Introduction.models import Introduction
from LiteratureManagement.models import Literature, LiteratureCategory
from ImageManagement.models import Images, ImageCategory
from VideoManagement.models import Videos, VideoCategory
from DataManagement.models import Data, DataCategory


def index(request):
    '''首页'''
    literatures = Literature.objects.order_by('-create_date')[:5]
    datas = Data.objects.order_by('-create_date')[:5]
    return render(request, 'home/index.html', locals())


def introduction(request):
    '''简介'''
    info = Introduction.objects.order_by('-create_date')[0]
    return render(request, 'home/details.html', locals())


def datas(request):
    '''列表页'''
    dataCategorys = DataCategory.objects.\
        all().order_by("category_name")
    if 'category' not in request.GET or '所有类别' == request.GET['category'] or\
            '' == request.GET['category']:
        category_name = '所有类别'
        datas = Data.objects.order_by('-create_date')
    else:
        category_name = request.GET['category']
        datas = DataCategory.objects.get(category_name=category_name)\
            .data_set.all().order_by('-create_date')
    # 对结果进行分页
    p = Paginator(datas, 15)
    pages = p.page_range
    page = int(request.GET.get('page', 1))
    if not (0 < page <= p.num_pages):
        page = 1
    page_start = page - 3 if page - 3 > 0 else 1
    page_end = page + 3 if page + 3 < p.num_pages else p.num_pages
    if page_start == page_end:
        page_range = pages
    else:
        page_range = pages[page_start - 1:page_end]
    print(page_range, page_start, page_end)
    result_page = p.page(page)
    infos = result_page.object_list
    return render(request, 'home/list.html',
                  {
                      'result_page': result_page,
                      'category_name': category_name,
                      'dataCategorys': dataCategorys,
                      'infos': infos,
                      'page': page,
                      'pages': page_range,
                      'num_pages': p.num_pages
                  })


def data(request, article_id):
    info = Data.objects.get(id=article_id)
    return render(request, 'home/details.html', locals())


def literatures(request):
    '''列表页'''
    dataCategorys = LiteratureCategory.objects.\
        all().order_by("category_name")
    if 'category' not in request.GET or '所有类别' == request.GET['category'] or\
            '' == request.GET['category']:
        category_name = '所有类别'
        datas = Literature.objects.order_by('-create_date')
    else:
        category_name = request.GET['category']
        datas = LiteratureCategory.objects.get(category_name=category_name)\
            .literature_set.all().order_by('-create_date')
    # 对结果进行分页
    p = Paginator(datas, 15)
    pages = p.page_range
    page = int(request.GET.get('page', 1))
    if not (0 < page <= p.num_pages):
        page = 1
    page_start = page - 3 if page - 3 > 0 else 1
    page_end = page + 3 if page + 3 < p.num_pages else p.num_pages
    if page_start == page_end:
        page_range = pages
    else:
        page_range = pages[page_start - 1:page_end]
    print(page_range, page_start, page_end)
    result_page = p.page(page)
    infos = result_page.object_list
    return render(request, 'home/literatures.html',
                  {
                      'result_page': result_page,
                      'category_name': category_name,
                      'dataCategorys': dataCategorys,
                      'infos': infos,
                      'page': page,
                      'pages': page_range,
                      'num_pages': p.num_pages
                  })


def literature(request, article_id):
    info = Literature.objects.get(id=article_id)
    return render(request, 'home/details.html', locals())


def images(request):
    '''列表页'''
    dataCategorys = ImageCategory.objects.\
        all().order_by("category_name")
    if 'category' not in request.GET or '所有类别' == request.GET['category'] or\
            '' == request.GET['category']:
        category_name = '所有类别'
        datas = Images.objects.order_by('-create_date')
    else:
        category_name = request.GET['category']
        datas = ImageCategory.objects.get(category_name=category_name)\
            .images_set.all().order_by('-create_date')
    # 对结果进行分页
    p = Paginator(datas, 15)
    pages = p.page_range
    page = int(request.GET.get('page', 1))
    if not (0 < page <= p.num_pages):
        page = 1
    page_start = page - 3 if page - 3 > 0 else 1
    page_end = page + 3 if page + 3 < p.num_pages else p.num_pages
    if page_start == page_end:
        page_range = pages
    else:
        page_range = pages[page_start - 1:page_end]
    print(page_range, page_start, page_end)
    result_page = p.page(page)
    infos = result_page.object_list
    return render(request, 'home/images.html',
                  {
                      'result_page': result_page,
                      'category_name': category_name,
                      'dataCategorys': dataCategorys,
                      'infos': infos,
                      'page': page,
                      'pages': page_range,
                      'num_pages': p.num_pages
                  })


def image(request, article_id):
    info = Images.objects.get(id=article_id)
    return render(request, 'home/details.html', locals())


def videos(request):
    '''列表页'''
    dataCategorys = VideoCategory.objects.\
        all().order_by("category_name")
    if 'category' not in request.GET or '所有类别' == request.GET['category'] or\
            '' == request.GET['category']:
        category_name = '所有类别'
        datas = Videos.objects.order_by('-create_date')
    else:
        category_name = request.GET['category']
        datas = VideoCategory.objects.get(category_name=category_name)\
            .videos_set.all().order_by('-create_date')
    # 对结果进行分页
    p = Paginator(datas, 15)
    pages = p.page_range
    page = int(request.GET.get('page', 1))
    if not (0 < page <= p.num_pages):
        page = 1
    page_start = page - 3 if page - 3 > 0 else 1
    page_end = page + 3 if page + 3 < p.num_pages else p.num_pages
    if page_start == page_end:
        page_range = pages
    else:
        page_range = pages[page_start - 1:page_end]
    print(page_range, page_start, page_end)
    result_page = p.page(page)
    infos = result_page.object_list
    return render(request, 'home/videos.html',
                  {
                      'result_page': result_page,
                      'category_name': category_name,
                      'dataCategorys': dataCategorys,
                      'infos': infos,
                      'page': page,
                      'pages': page_range,
                      'num_pages': p.num_pages
                  })


def video(request, article_id):
    info = Videos.objects.get(id=article_id)
    return render(request, 'home/details.html', locals())
