# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Videos, VideoCategory
from .forms import VideosForm


class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'last_update_date')
    search_fields = ('title', 'author__username')
    form = VideosForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(VideosAdmin, self).get_form(request, obj, **kwargs)
        form.author = request.user
        return form

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Videos, VideosAdmin)
admin.site.register(VideoCategory, VideoCategoryAdmin)
