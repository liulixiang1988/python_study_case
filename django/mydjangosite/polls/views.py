# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('你好，这是投票应用的首页')
