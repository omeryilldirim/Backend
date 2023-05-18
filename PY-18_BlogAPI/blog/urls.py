from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CategoryViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('categories', CategoryViewSet)

url_patterns = router.urls