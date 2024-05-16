from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
#from django.contrib.auth.forms import UserCreationForm #for creating the from from django 
from .forms import UserRegisterForm,UserUpdateForm , ProfileUpdateForm #using it in the place of  Usercreation 


# Create your views here.

def register(request):
    if request.method =='POST':     
        form =UserRegisterForm(request.POST)                     #instantiating the form if we get any post request of user form 
        if form.is_valid():
            user=form.save(True) 
            Profile.objects.create(user=user)                                         #it will save and hashed the password 
            username = form.cleaned_data.get('username')  
                     #cleaned_data is dict where the data will be stored 
            messages.success(request,f'Account created for {username}! You can Login Now.')
            return redirect('login')                                           #redirecting by blog_app home 
    else:
        form = UserRegisterForm()    
    return render(request, 'users/register.html', {'form': form}) #passing the form as a context so we can access form within the template


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method =='POST':            
        u_form = UserUpdateForm(request.POST, instance=request.user)                  #instanciating the form in login required
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Profile has been updated')
            return redirect('profile')  #for avoiding the get request from the browser
    else:
        u_form = UserUpdateForm(instance=request.user)                   
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    #passing the  form to template by context
    context ={
            'u_form': u_form,
            'p_form': p_form
    }
    return render(request , 'users/profile.html',context)

# message.debug
# message.info , messages.success, message.warning, message.error