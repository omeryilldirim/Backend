from rest_framework import routers
from django.urls import path
from .views import QueryView, ReservationViewSet

urlpatterns = [
    path('query/', QueryView.as_view())
]
router = routers.DefaultRouter()
# router.register('car', CarViewSet)
# router.register('customer', CustomerViewSet)
router.register('reservation', ReservationViewSet)


urlpatterns += router.urls