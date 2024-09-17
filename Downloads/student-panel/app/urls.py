from django.urls import path
from .views import index,signup,ragistration,dashboard,login,course,addcourse
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",index, name="index"),
    path("signup/",signup,name='signup'),
    path("ragistration/",ragistration),
    path("dashboard/",dashboard,name='dashboard'),
    path("login/",login),
    path("course/",course,name='course'),
    path("addcourse/", addcourse)
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
