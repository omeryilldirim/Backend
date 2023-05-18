from rest_framework.routers import DefaultRouter
from blog.views import PostView, CategoryView


router = DefaultRouter()
router.register('posts', PostView)
router.register('categories', CategoryView)
urlpatterns = router.urls