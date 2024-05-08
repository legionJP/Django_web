from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): #for adding the email in usercreation form
    email = forms.EmailField() #required = True by default

    class Meta:    #Thsis class gives us the nested namspace for the configurtion and keeps the configuration in one place
        model = User
        fields = ['username','email','password1','password2']