from rest_framework import serializers
from .models import Car, Reservation, Customer, Query
from rest_framework.response import Response
from rest_framework import status


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class QuerySerializer(serializers.ModelSerializer):
    available_cars = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Query
        fields = '__all__'

    def get_available_cars(self, obj):
        reserved_cars = Reservation.objects.filter(
            start_date__lte=obj.start_date, 
            end_date__gte=obj.start_date
        ).values_list('car', flat=True)
        return CarSerializer(Car.objects.exclude(id__in=reserved_cars), many=True).data

    def validate(self, data, *args, **kwargs):
        from django.utils import timezone
        now = timezone.now()
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        if data['start_date'] < now.date():
            raise serializers.ValidationError("Start date can not be in the past.")
        if data['end_date'] <= now.date():
            raise serializers.ValidationError("End date must be in the future.")
        return data    


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data, *args, **kwargs):
        from django.utils import timezone
        now = timezone.now()
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        if data['start_date'] < now.date():
            raise serializers.ValidationError("Start date can not be in the past.")
        if data['end_date'] <= now.date():
            raise serializers.ValidationError("End date must be in the future.")
        return data
    
    def create(self, validated_data):
        reserved_cars = Reservation.objects.filter(
            start_date__range=[validated_data['start_date'], validated_data['end_date']],
            # end_date__gte=validated_data['end_date']
            end_date__range=[validated_data['start_date'], validated_data['end_date']]
        ).values_list('car', flat=True)
        print(reserved_cars)
        print(validated_data['car'].id)
        if validated_data['car'].id in reserved_cars:
            raise serializers.ValidationError("Car is not available for this date range.")
        return Reservation.objects.create(**validated_data)
    
