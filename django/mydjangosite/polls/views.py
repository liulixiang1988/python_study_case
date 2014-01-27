# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Poll


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    return HttpResponse('投票%s的细节' % poll_id)


def results(request, poll_id):
    return HttpResponse('投票%s的结果' % poll_id)


def vote(request, poll_id):
    return HttpResponse('对投票%s进行投票' % poll_id)

