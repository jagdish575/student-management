from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=255)

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    fees = models.IntegerField(max_length=200)
    duraction = models.CharField(max_length=200)
