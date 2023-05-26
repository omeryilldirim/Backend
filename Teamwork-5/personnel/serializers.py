from rest_framework import serializers
from .models import Personnel, Department


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        exclude= []


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        exclude= []
