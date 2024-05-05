from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

#creating logic to handle the routes 


posts = [
    {
        "author": "Author1",
        "title": "Title1",
        "content": "Content1",
        "date_posted": "2024-05-01"
    },
    {
        "author": "Author2",
        "title": "Title2",
        "content": "Content2",
        "date_posted": "2024-05-02"
    },
    {
        "author": "Author3",
        "title": "Title3",
        "content": "Content3",
        "date_posted": "2024-05-03"
    },
    {
        "author": "Author4",
        "title": "Title4",
        "content": "Content4",
        "date_posted": "2024-05-04"
    },
    {
        "author": "Author5",
        "title": "Title5",
        "content": "Content5",
        "date_posted": "2024-05-05"
    }
]


def home(request):
    context ={
        'posts':posts   #posts variable will be equal to post data which is equal to posts data 
    }
    #return HttpResponse('<h1> Blog Home </h1>')
    return render(request,'blog_app/home.html',context)  #this render template still retrun the htpp response in background

def about(request):
    #return HttpResponse('<h1> About Page </h1>')
    return render(request,'blog_app/about.html',{'title':'About'}) #passing the default title 