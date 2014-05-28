from django.contrib import admin

# Register your models here.
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)