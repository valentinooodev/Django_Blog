from django.db.models import fields
from rest_framework import serializers
from blog.models import Post, Series, SubPost

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ('category', 'title', 'slug', 'author', 'description', 'image', 'content', 'is_active')
        model = Post


class SeriesSerializer(serializers.ModelSerializer):
    fields = ('category', 'author', 'title', 'slug', 'description', 'content', 'image')


class SubPostSerializer(serializers.ModelSerializer):
    fields = ('series', 'title', 'slug', 'description', 'index', 'content', 'is_active')