from rest_framework import routers
from .views import CarViewSet, CustomerViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register('car', CarViewSet)
router.register('customer', CustomerViewSet)
router.register('reservation', ReservationViewSet)

urlpatterns = router.urls