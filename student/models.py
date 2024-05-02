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
    
