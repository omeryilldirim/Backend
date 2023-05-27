from rest_framework import serializers
from .models import Personnel, Department


class PersonnelSerializer(serializers.ModelSerializer):
    # department = serializers.StringRelatedField()
    # department_id = serializers.IntegerField()
    # department = serializers.SerializerMethodField()
    # gender = serializers.StringRelatedField()
    class Meta:
        model = Personnel
        exclude =[]

    # def get_department(self, obj):
    #     return obj.department.name
    
    # def get_gender(self, obj):
    #     return obj.get_gender_display()

class DepartmentSerializer(serializers.ModelSerializer):
    department_personnel = PersonnelSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        exclude= []
