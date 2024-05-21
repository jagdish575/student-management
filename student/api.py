from .models import *
from .serializers import UserSerializers,CourseSerializers,Studentserializers
from  rest_framework import generics


class CreateUserApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class ItemList(generics.ListAPIView):
    queryset= User.objects.all()
    serializer_class=UserSerializers

class CreateCourseApi(generics.ListAPIView):
    queryset= Course.objects.all()
    serializer_class=CourseSerializers


class CreateStudentApi(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class=Studentserializers

class CourseupdateApi(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class=CourseSerializers

class CoursedeleteAPi(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

class StudentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class =Studentserializers

class StudentdeleteApi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class =Studentserializers




