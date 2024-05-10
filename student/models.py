from django.db import models


# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)



class Course(models.Model):
    course_name= models.CharField(max_length=100)
    fees= models.IntegerField()
    duration= models.CharField(max_length=20)
    

class Student (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile = models.IntegerField(default=0)
    college=models.CharField(max_length=200)
    degree=models.CharField(max_length=200)
    course=models.ForeignKey( Course,on_delete=models.CASCADE)
    address=models.TextField()
    image=models.FileField(upload_to='student/',max_length=100)
    



