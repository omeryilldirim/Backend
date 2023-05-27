from rest_framework import serializers
from .models import Personnel, Department


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        exclude= []


class DepartmentSerializer(serializers.ModelSerializer):
    department_personnel = PersonnelSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        exclude= []
