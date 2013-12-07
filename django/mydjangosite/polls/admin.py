__author__ = 'liulixiang'

from django.contrib import admin
from polls.models import Choice, Poll


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('日期信息', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
