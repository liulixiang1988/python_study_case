# -*- coding:utf-8 -*-
from django.forms import ModelForm
from .models import Data


class DataForm(ModelForm):

    class Meta:
        model = Data
        fields = ['title',
                  'content',
                  'categorys']
