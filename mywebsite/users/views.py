from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm #for creating the from from django 
from .forms import UserRegisterForm #using it in the place of  Usercreation 


# Create your views here.

def register(request):
    if request.method =='POST':     
        form =UserRegisterForm(request.POST) #instantiating the form if we get any post request of user form 
        if form.is_valid():
            form.save()  #it will save and hashed the password 
            username = form.cleaned_data.get('username') #cleaned_data is dict where the data will be stored 
            messages.success(request,f'Account created for {username}! You can Login Now.')
            return redirect('login') #redirecting to the  home by name of the blog_app home 
    else:
        form = UserRegisterForm()    
    return render(request, 'users/register.html', {'form': form}) #passing the form as a context so we can access form within the template

@login_required
def profile(request):
    return render(request , 'users/profile.html')

# message.debug
# message.info , messages.success, message.warning, message.error