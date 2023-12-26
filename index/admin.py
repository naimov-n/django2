from django.contrib import admin

# Register your models here.
from index.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'created_on', 'status')
    list_display_links = ('id',)
    search_fields = ('title', 'content')
    list_editable = ('status',)
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('status',)
    list_filter = ('status',)


class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('status',)
    list_filter = ('status',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Social, SocialAdmin)