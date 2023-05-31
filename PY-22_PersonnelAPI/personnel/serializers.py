from rest_framework import serializers
from .models import Department, Personnel


class PersonnelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Personnel
        fields = ('first_name', 'last_name', 'title')


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'

class DepartmentPersonnelSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'

