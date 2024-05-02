from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.http import HttpResponse 


def create_user(request):
    if request.method == "POST":
        username = request.POST['name']  
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")
        else:
            new_user = User.objects.create(name=username, email=email, password=password)
            return HttpResponse("sign-in/")
        


def sign_in(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            password=user.password
            if check_password(password,user.password):
                return HttpResponse("done")
            else:
                return HttpResponse("Password incorrected ")
        else:
            return HttpResponse("Email not registered")
    # else:
        # Handle GET request if needed
        # return render(request, 'login.html')



        

def index(request):
    return render(request, 'index.html')

def sign_up(request):
    return render(request, 'sign-up.html')

def Profile(request):
    return render(request, 'profile.html')

def course(request):
    return render(request,'courses.html')


def add_courses(request):
    if request.method == "POST":
        course_name = request.POST['couses']
        fees = request.POST['fees']
        duration=request.POST['duration']
        if Course.objects.filter(course_name=course_name).exists():
            return HttpResponse("Course Already Exists")
        else:
            Course.objects.create(course_name=course_name, fees=fees,
                                  duration=duration)
            return redirect("/course/")
        
def course(request):
    db = Course.objects.all()
    return render(request, "courses.html", {'data':db})






