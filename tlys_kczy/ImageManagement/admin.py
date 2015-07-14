# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Images
from .forms import ImagesForm


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'last_update_date')
    search_fields = ('title', 'author__username')
    form = ImagesForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(ImagesAdmin, self).get_form(request, obj, **kwargs)
        form.author = request.user
        return form

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Images, ImagesAdmin)
