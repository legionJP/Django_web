from django.shortcuts import render
from .models import Post
#import the list views for the homepage 
from django.views.generic import ListView , DetailView
#from django.http import HttpResponse

# Create your views here.
#creating logic to handle the routes 

def home(request):  #this is function view 
    context ={
        'posts':Post.objects.all()   #posts variable will be equal to post data which is equal to posts data 
    }
    #return HttpResponse('<h1> Blog Home </h1>')
    return render(request,'blog_app/home.html', context)  #this render template still retrun the htpp response in background

#class view of listview
class PostListView(ListView):
    model = Post    #querying the post model 
    template_name = 'blog_app/home.html'
    context_object_name = 'posts' #bcz list view will be looking the post as the object name
    ordering = ['-date_posted']

class PostDetailView(DetailView): #here django will be looking for the Detail.html, without specifying template name
    model = Post




def about(request):
    #return HttpResponse('<h1> About Page </h1>')
    return render(request,'blog_app/about.html', {'title':'About'}) #passing the default title 



