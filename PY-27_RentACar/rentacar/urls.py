from django.urls import path, include

urlpatterns = [
]

# --------------------------------
# Routers
# --------------------------------

from rest_framework.routers import DefaultRouter
from .views import CarViewSet, ReservationViewSet

router = DefaultRouter()
router.register('car', CarViewSet)
router.register('reservation', ReservationViewSet)

urlpatterns += router.urls