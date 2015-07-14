from django.contrib import admin

from .models import Introduction


class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'last_update_date')
    search_fields = ('title',)

admin.site.register(Introduction, IntroductionAdmin)
