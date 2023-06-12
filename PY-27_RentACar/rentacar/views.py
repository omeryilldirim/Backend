from .serializers import(
    Car, CarSerializer,
    Reservation, ReservationSerializer,
)
from rest_framework.viewsets import ModelViewSet


# -------------------------------
# FixViewSet
# -------------------------------
class FixViewSet(ModelViewSet):
    pass


# -------------------------------
# CarViewSet
# -------------------------------
class CarViewSet(FixViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# -------------------------------
# ReservationViewSet
# -------------------------------
class ReservationViewSet(FixViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer