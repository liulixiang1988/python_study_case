from django.contrib import admin

from gr_users.models import GRUser


class GRUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(GRUser, GRUserAdmin)