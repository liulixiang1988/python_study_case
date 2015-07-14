from django.contrib import admin
from .models import Data, DataCategory
from .forms import DataForm


class DataAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'last_update_date')
    search_fields = ('title', 'author__username')
    form = DataForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(DataAdmin, self).get_form(request, obj, **kwargs)
        form.author = request.user
        return form

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class DataCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

admin.site.register(Data, DataAdmin)
admin.site.register(DataCategory, DataCategoryAdmin)
