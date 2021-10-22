from django.contrib import admin
from django.db import models

from . models import Category, Post, Series, SubPost


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'author', 'description', 'image', 'content', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_active']

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['category', 'author', 'title', 'slug', 'description', 'content', 'image']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(SubPost)
class SubPostAdmin(admin.ModelAdmin):
    list_display = ['series', 'title', 'slug', 'description', 'index', 'content', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_active']