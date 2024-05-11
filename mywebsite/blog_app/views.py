from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from .models import Post 
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#import the list views for the homepage 
from django.views.generic import (ListView , 
                DetailView , CreateView,UpdateView,DeleteView)
#from django.http import HttpResponse
# Create your views here.
#creating logic to handle the routes 

#------------------------------------------------------------------
def home(request):  #this is function view 
    context ={
        'posts':Post.objects.all()   #posts variable will be equal to post data which is equal to posts data 
    }
    #return HttpResponse('<h1> Blog Home </h1>')
    return render(request,'blog_app/home.html', context)  #this render template still retrun the htpp response in background

#---------------------------------------------------------------#
#class view of listview
class PostListView(ListView):
    model = Post    #querying the post model 
    template_name = 'blog_app/home.html'
    context_object_name = 'posts' #bcz list view will be looking the post as the object name
    ordering = ['-date_posted']
    paginate_by = 5

#--------------------------------------------------------------------------------------

class UserPostListView(ListView):
    model = Post    #querying the post model 
    template_name = 'blog_app/user_posts.html'
    context_object_name = 'posts' #bcz list view will be looking the post as the object name
    #ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username')) #KWARGS IS query param
        return Post.objects.filter(author = user).order_by('-date_posted')
         

#--------------------------------------------------------------------#
class PostDetailView(DetailView): #here django will be looking for the Detail.html, without specifying template name
    model = Post
#------------------------------------------------------------------------#
class PostCreateView(LoginRequiredMixin,CreateView):  
    model = Post
    fields =['title', 'content']

    #overriding the form create method 
    def form_valid(self, form):
        form.instance.author = self.request.user #author will be cureent login user
        return super().form_valid(form)
#----------------------------------------------------------------------#
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):  
    model = Post
    fields =['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user #author will be cureent login user
        return super().form_valid(form)
    
    #userpassestest mixin to avoid update by others
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        # return super().test_func()
#--------------------------------------------------------------------
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): #here django will be looking for the Detail.html, without specifying template name
    model = Post 
    success_url = '/'
    #userpassestest mixin to avoid delete by others
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 
#-----------------------------------------------------------
def about(request):
    #return HttpResponse('<h1> About Page </h1>')
    return render(request,'blog_app/about.html', {'title':'About'}) #passing the default title 



