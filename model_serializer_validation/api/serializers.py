from rest_framework import serializers
from .models import Student




class StudentSerializer(serializers.ModelSerializer):

    # Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with R')

    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('SEAT FULL')
        return value


    # Object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'tom' and ct.lower() != 'sf':
            raise serializers.ValidationError('error city is SF')
        return data
