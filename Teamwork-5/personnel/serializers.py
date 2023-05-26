from rest_framework import serializers
from .models import Personnel, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude= []


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        exclude= []

