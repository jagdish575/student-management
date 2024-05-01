from django.urls import path
from .views import *

urlpatterns = [
    path('', index),          
   path('registration/',create_user),
   path('signup/',sign_up),
   path('sign-in/', sign_in,),
]