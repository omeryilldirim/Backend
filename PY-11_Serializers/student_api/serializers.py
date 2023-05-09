from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name= validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'number']
        # fields = '__all__'
        # exclude = ['number']
        # read_only_fields = ['first_name', 'last_name']
        # extra_kwargs = {
        #     'first_name': {'read_only': True}
        # }
