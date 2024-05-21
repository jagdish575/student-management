from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ='__all__'