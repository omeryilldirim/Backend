from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CarSerializer, Car, 
    ReservationSerializer, Reservation,
    CustomerSerializer, Customer, 
)

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer