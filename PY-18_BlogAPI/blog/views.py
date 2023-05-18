from .serializers import (
    PostSerializer, CategorySerializer, 
    Post, Category
)
from rest_framework.viewsets import ModelViewSet

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer