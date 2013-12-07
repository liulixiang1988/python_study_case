__author__ = 'liulixiang'

from django.contrib import admin
from polls.models import Poll


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('日期信息', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]


admin.site.register(Poll, PollAdmin)
