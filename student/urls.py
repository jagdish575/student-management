from django.urls import path
from .views import *

urlpatterns = [
    path('', Profile),        
    path('registration/', create_user),
    path('signup/', sign_up),
    path('sign-in/', sign_in,),
    path('course/', course),
    path('addcourse/', add_courses),
]