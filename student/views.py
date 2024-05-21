from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.http import HttpResponse 
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def sign_in(request):
    if request.method=='POST':
        email=request.POST.get('email')
        user_password=request.POST.get('password')
        if User.objects.filter(email=email).exists():
            obj=User.objects.get(email=email)
            password=obj.password
            if check_password(user_password,password):
                return redirect('/profile/')
            else:
                messages.error( request, "Password incorrected ")
                return redirect('/')
        else:
             messages.error( request , "Email not registered")
             return redirect('/')
    

def sign_up(request):
    return render(request, 'sign-up.html')

def create_user(request):
    if request.method=="POST":
        name = request.POST['name']
        email=request.POST['email']
        password=make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            return HttpResponse("Already Exist")
        else:
            User.objects.create(name=name,email=email,password=password)
            return redirect("/")
        


def delete_course(request, pk):
         dt = Course.objects.get(id=pk)
         dt.delete()
         return redirect('/courses/')

def update_course( request,uid):
    course = Course.objects.get( id = uid )
    return render(request, 'course_update.html',{ 'course': course } )

    
def course_update(request,):
    if request.method == 'POST':
        uid=request.POST['uid']
        course_name=request.POST['couses']
        fees=request.POST['fees']
        duration=request.POST['duration']
        Course.objects.filter(id=uid).update(course_name=course_name,fees=fees,duration=duration)
        return redirect('/course/')

   
def profile(request,pk):
    student_obj=Student.objects.get(id=pk)
    return render(request, 'profile.html', { 'student_obj':student_obj } )




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
            Course.objects.create(course_name=course_name, fees=fees,duration=duration)
            return redirect("/course/")
        
def course(request):
    db = Course.objects.all()
    return render(request, "courses.html", {'data':db})


def view_students(request):
    course_obj=Course.objects.all()
    student_obj=Student.objects.all()
    return render(request,'viewstudents.html',{ 'course_obj':course_obj ,'student_obj':student_obj})


def add_student(request):
    if request.method=="POST" :
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        college= request.POST['college']
        address =request.POST['address']
        degree=request.POST['degree']
        course_id=request.POST['course']
        new_course=Course.objects.get(id=course_id)
        image=request.FILES.get('image')
        if Student.objects.filter(email=email).exists():
            return HttpResponse('Student already exists!')
        else:
            Student.objects.create(name=name,email=email,mobile=mobile,college=college, address=address,degree=degree, course=new_course,image=image)
            return redirect("/student/")
        




def dashboard(request):
    return render (request ,'dashboard.html')






