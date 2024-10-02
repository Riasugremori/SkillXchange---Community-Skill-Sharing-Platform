from rest_framework import serializers
from .models import Course, CourseRate 

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' 

class CourseRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRate
        fields = '__all__' 
