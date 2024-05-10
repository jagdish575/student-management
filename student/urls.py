from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),        
    path('registration/', create_user),
    path('signup/', sign_up),
    path('signin/', sign_in,),
    path('course/', course),
    path('addcourse/', add_courses),
    path('profile/',Profile),
    path('courseupdate/',course_update),
    path('delete_course/<int:pk>/',delete_course, name='delete_course'),
    path('course_update/<int:uid>/', update_course, name='update_course'),
    path('student/', view_students,name='view_students'),
    path('addstudent/',add_student,name='add_student'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)