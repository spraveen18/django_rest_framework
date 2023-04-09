from rest_framework import serializers
from .models import Student

# will work for all crud operation
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['name', 'roll', 'city']


class StudentSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(read_only=True)  # name will not update
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll'] # both name roll will not update
        extra_kwargs = {'name':{'read_only':True}}
