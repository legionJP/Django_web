from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one realtionship with profile user , cascade- delete user then delete profile
    image = models.ImageField(default='default.jpg',upload_to='profile_pics') #profile_pics the directory
    
    def __str__(self):
        return f'{self.user.username} Profile' 
    
    #run the migrations