# -*- coding:utf-8 -*-
from django.forms import ModelForm
from .models import Images


class ImagesForm(ModelForm):

    class Meta:
        model = Images
        fields = ['title',
                  'content', 'categorys']
