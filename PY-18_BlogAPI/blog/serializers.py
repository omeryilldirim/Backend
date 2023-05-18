from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []
        
