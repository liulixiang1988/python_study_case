# -*- coding:utf-8 -*-
__author__ = 'liulixiang'

from django import forms
from .models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="请输入类型名称")
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Category


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="请输入标题")
    url = forms.URLField(max_length=128, help_text="请输入网页地址")
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Page



