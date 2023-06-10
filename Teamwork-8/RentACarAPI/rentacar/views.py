from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import (
    Car, 
    Reservation,
    Customer,
    Query, QuerySerializer, 
    ReservationSerializer, 
)

class QueryView(generics.ListCreateAPIView):
    serializer_class = QuerySerializer
    queryset = Query.objects.all()


class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()