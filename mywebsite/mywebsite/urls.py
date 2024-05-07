"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

from users import views as user_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name='register'), #dircetly adding route 
    path('',include('blog_app.urls'))  #leaving the route empty so that is will go to hme of the blog_app

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   
   #including the path from blog_app in project, here the include 
     #is chopping off the blog_app from .urls because first it goes to blog_app already 
            #returning the empty string 
