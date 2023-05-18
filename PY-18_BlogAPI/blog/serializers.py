from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class PostSerializer(serializers.ModelSerializer):
    user  = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    class Meta:
        model = Post
        exclude = [
            # 'created_date',
            # 'updated_date',
        ]
        
