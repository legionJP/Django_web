from django.shortcuts import render
from .models import Post

#from django.http import HttpResponse

# Create your views here.

#creating logic to handle the routes 

def home(request):
    context ={
        'posts':Post.objects.all()   #posts variable will be equal to post data which is equal to posts data 
    }
    #return HttpResponse('<h1> Blog Home </h1>')
    return render(request,'blog_app/home.html', context)  #this render template still retrun the htpp response in background

def about(request):
    #return HttpResponse('<h1> About Page </h1>')
    return render(request,'blog_app/about.html', {'title':'About'}) #passing the default title 