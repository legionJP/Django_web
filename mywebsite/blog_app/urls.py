from django.urls import path
from .views import (PostListView , 
         PostDetailView,PostCreateView, PostUpdateView,PostDeleteView)
from . import views #importing the views from current directory 

urlpatterns = [
    #path('',views.home, name='blog_app-home'), #empty path for home page  #the pattern of empty route is manage by the views.home
    path('',PostListView.as_view(), name='blog_app-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #particular route for post
    path('post/new/', PostCreateView.as_view(), name='post-create'), #particular route for post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Using the post-form template and particular route for post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
        # this will use the post_confirm_delete.html template and  
    
    path('about/',views.about, name='blog_app-about'),
]

# #looking the template of 
# <app>/<model><viewtype>.html
# blog_app/post_list.html