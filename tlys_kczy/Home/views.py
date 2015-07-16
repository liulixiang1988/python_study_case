from django.shortcuts import render
from LiteratureManagement.models import Literature, LiteratureCategory
from DataManagement.models import Data, DataCategory


def index(request):
    '''首页'''
    literatures = Literature.objects.order_by('-create_date')[:5]
    datas = Data.objects.order_by('-create_date')[:5]
    return render(request, 'home/index.html', locals())


def list(request):
    '''列表页'''
    literatureCategorys = LiteratureCategory.objects.\
        all().order_by("category_name")
    dataCategorys = DataCategory.objects.\
        all().order_by("category_name")
    return render(request, 'home/list.html', locals())
