from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #Django created the user model in this location 
from django.urls import reverse
# Create your models here.

class Post(models.Model): #inheriting model form models , so each class is now going to be it's own table in database
    title= models.CharField(max_length=100) #title is aatribute of table , each attribute will be different field in database
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # or can use: auto_now_add=True, for last_update 
    author = models.ForeignKey(User, on_delete=models.CASCADE) #the post models having relation to user as a one to Many

#applying __str__ method to see the models's data as a descriptive
    def __str__(self):
        return self.title
         
#reverse function for returning the the url as a string and the view will handle it 
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    