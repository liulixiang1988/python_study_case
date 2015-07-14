# -*- coding:utf-8 -*-
from django.contrib import admin
from django.forms import TextInput
from django.db import models
from .models import (Data, DataCategory, Introduction, Literature, LiteratureCategory)
from .forms import LiteratureForm


class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'last_update_date')
    search_fields = ('title',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'width': '100%'})},
    }


class DataAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'last_update_date')
    search_fields = ('title', )


class DataCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


class LiteratureAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'last_update_date')
    search_fields = ('title', 'author__username')
    form = LiteratureForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(LiteratureAdmin, self).get_form(request, obj, **kwargs)
        form.author = request.user
        return form

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class LiteratureCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(DataCategory, DataCategoryAdmin)
admin.site.register(Literature, LiteratureAdmin)
admin.site.register(LiteratureCategory, LiteratureCategoryAdmin)
