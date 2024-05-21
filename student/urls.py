from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .api import *

urlpatterns = [
    path('', index),        
    path('registration/', create_user),
    path('signup/', sign_up),
    path('signin/', sign_in,),
    path('courses/', course),
    path('addcourse/', add_courses),
    path('profile/<int:pk>/',profile, name='profile'),
    path('courseupdate/',course_update),
    path('delete_course/<int:pk>/',delete_course, name='delete_course'),
    path('course_update/<int:uid>/', update_course, name='update_course'),
    path('student/', view_students,name='view_students'),
    path('addstudent/',add_student,name='add_student'),
    path('dashboard/',dashboard,name='dashboard'),
    # API URLS
    path('api/user',CreateUserApi.as_view()),
    path('api/get',ItemList.as_view()),
    path('api/course',CreateCourseApi.as_view()),
    path('student/course',CreateStudentApi.as_view()),
    path('update/<int:pk>/',CourseupdateApi.as_view()),
    path('delete/<int:pk>/',CoursedeleteAPi.as_view()),
    path('student/update/<int:pk>/',StudentUpdateApi.as_view()),
    path('student/delete/<int:pk>/',StudentdeleteApi.as_view()),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)