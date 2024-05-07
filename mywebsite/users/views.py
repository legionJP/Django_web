from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm #for creating the from from django Usercreation 


# Create your views here.

def register(request):
    if request.method =='POST':     
        form =UserCreationForm(request.POST) #instantiating the form if we get any post request of user form 
        if form.is_valid():
            username = form.cleaned_data.get('username') #cleaned_data is dict where the data will be stored 
            messages.success(request,f'Account created for {username}!')
            return redirect('blog_app/home.html') #redirecting to the  home by name of the blog_app home 
    else:
        form = UserCreationForm()    
    return render(request, 'users/register.html',{'form': form}) #passing the form as a context so we can access form within the template



# message.debug
# message.info , messages.success, message.warning, message.error