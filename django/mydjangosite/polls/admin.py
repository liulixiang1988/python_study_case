__author__ = 'liulixiang'

from django.contrib import admin
from polls.models import Poll


class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
