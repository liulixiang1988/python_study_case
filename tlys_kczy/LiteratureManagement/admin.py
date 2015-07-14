# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Literature, LiteratureCategory
from .forms import LiteratureForm


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

admin.site.register(Literature, LiteratureAdmin)
admin.site.register(LiteratureCategory, LiteratureCategoryAdmin)
