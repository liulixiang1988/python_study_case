# -*- coding:utf-8 -*-
from django.contrib import admin
from django.forms import TextInput
from django.db import models
from .models import Introduction


class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'last_update_date')
    search_fields = ('title',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'width': '100%'})},
    }

admin.site.register(Introduction, IntroductionAdmin)
