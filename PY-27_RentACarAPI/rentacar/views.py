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
from .permissions import IsStaffOrReadOnly
class CarViewSet(FixViewSet):
    queryset = Car.objects.filter(available=True)
    serializer_class = CarSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_staff: # staff ise tüm veriyi göster
            queryset = Car.objects.all()
        else:
            queryset = super().get_queryset() # değilse default veriyi göster -> Car.objects.filter(available=True)
        
        # http://localhost:8000/api/car?from=2023-01-20&to=2023-01-25
        start = self.request.query_params.get('from', None)
        end = self.request.query_params.get('to', None)

        if start and end:
            #! filter içinde or kullanamadığımız için bu yöntem sadece start date yönünden kontrol ediyor. aynısını end date için de yazmak lazım.
            # not_available_car_ids = Reservation.objects.filter(
            #     start_date__gte=start, start_date__lte=end
            # ).values_list('car_id', flat=True)
            # queryset = queryset.exclude(id__in=not_available_car_ids)

            # not_available_car_ids = Reservation.objects.filter(
            #     end_date__gte=start, end_date__lte=end
            # ).values_list('car_id', flat=True)
            # queryset = queryset.exclude(id__in=not_available_car_ids)

            #* AND ve OR kullanmak için Q parametresini kullabiliriz:
            from django.db.models import Q
            print(start, end)
            not_available_car_ids = Reservation.objects.filter(
                Q(start_date__gte = start, start_date__lte = end) | Q(end_date__gte = start, end_date__lte = end)
            ).values_list('car_id', flat=True)

            print(not_available_car_ids)
            
            queryset = queryset.exclude(id__in=not_available_car_ids)
            
        return queryset
    

# -------------------------------
# ReservationViewSet
# -------------------------------
from .permissions import IsOwnerOrStaff
class ReservationViewSet(FixViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsOwnerOrStaff]

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset() # Eğer user.is_staff ise default veriyi göster. 
        else:
            return Reservation.objects.filter(user=self.request.user) # Sadece kendi objelerini görsün.