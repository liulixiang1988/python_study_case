# -*- coding:utf-8 -*-
__author__ = 'liulixiang'

from django import forms
from django.contrib.auth.models import User
from .models import Category, Page, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="请输入类型名称")
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Category


class PageForm(forms.ModelForm):
    title = forms.CharField(label="标题", max_length=128, help_text="请输入标题",
                            widget=forms.TextInput(attrs={'placeholder': '请输入标题'}))
    url = forms.URLField(label="网址", max_length=128, help_text="请输入网页地址",
                         widget=forms.URLInput(attrs={'placeholder': '请输入网页地址'}))
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Page
        fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data


class UserForm(forms.ModelForm):
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))
    email = forms.EmailField(label='邮箱', widget=forms.EmailInput(attrs={'placeholder': '请输入邮箱'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    website = forms.CharField(label='网址', widget=forms.TextInput(attrs={'placeholder': '请输入网址'}), required=False)
    picture = forms.ImageField(label='头像', required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
