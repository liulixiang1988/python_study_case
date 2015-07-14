# -*- coding:utf-8 -*-
from django.forms import ModelForm
from .models import Literature


class LiteratureForm(ModelForm):

    class Meta:
        model = Literature
        fields = ['title',
                  'content',
                  'categorys']
