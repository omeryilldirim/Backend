from rest_framework import serializers
from .models import Department, Personnel


class PersonnelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personnel
        fields = '__all__'