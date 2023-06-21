from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls'))
]

# --------------------------------
# Routers
# --------------------------------
from .views import UserView, UserCreateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('create', UserCreateView) # allow any
router.register('', UserView) # only admin

urlpatterns += router.urls