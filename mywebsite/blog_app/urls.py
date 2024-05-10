from django.urls import path
from .views import PostListView ,  PostDetailView
from . import views #importing the views from current directory 

urlpatterns = [
    #path('',views.home, name='blog_app-home'), #empty path for home page  #the pattern of empty route is manage by the views.home
    path('',PostListView.as_view(), name='blog_app-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #particular route for post
    path('about/',views.about, name='blog_app-about'),
]

# #looking the template of 
# <app>/<model><viewtype>.html
# blog_app/post_list.html