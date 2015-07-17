# -*- coding:utf-8 -*-
from django.forms import ModelForm
from .models import Videos


class VideosForm(ModelForm):

    class Meta:
        model = Videos
        fields = ['title', 'content', 'categorys']
