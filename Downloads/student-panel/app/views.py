from django.shortcuts import render, redirect
from .models import Course,User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    return render(request, 'signup.html')


def dashboard(request):
    courses_obj = Course.objects.all().count()
    return render(request, "dashboard.html", {"courses_obj":courses_obj})


def course(request):
    course_obj = Course.objects.all()
    return render(request, "courses.html", {"course_obj": course_obj})

def ragistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already Exist")
        else:
            User.objects.create(name=name, email=email, password=password)
            return redirect("/")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        User_password = request.POST["password"]
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password
            if check_password(User_password, password):
                return redirect("/dashboard/")
            else:
                messages.error(request, "Password incorrect")
                return redirect("/")
        else:
            messages.error(request, "Email Not Ragister:")
            return redirect("/")


def addcourse(request):
    if request.method == "POST":
        course_name = request.POST.get("course")
        fees = request.POST.get("fees")
        duraction = request.POST.get("duraction")
        if Course.objects.filter(course_name = course_name).exists():
            messages.error(request, "This Name Alredy exists")
        else:
            Course.objects.create(course_name=course_name,fees=fees,
                                  duraction=duraction)
            return redirect("/course/")    
