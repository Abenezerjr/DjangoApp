from django.shortcuts import render ,  redirect
from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
# Create your views here.


def loginPage(request):
    page="login"
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username,password=password)
        except:
            messages.error(request,'Username does not exist')


        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user) # this create session in the database get that session and add in the browther coockis
            print('User is sccsessfulliy login')
            return redirect('profile')

        else:
            messages.error(request,"User name or password in correct")


    return render(request,'users/logInandRegistertionPage.html')

def logOutPage(request):

    logout(request)
    messages.error(request, 'User loged out!! ')
    return redirect('login')

def registerUser(request):
    page="register"
    form=CustomUserCreationForm()
    if request.method =="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False) # hold a temporay user request
            user.username=user.username.lower()
            user.save()
            messages.success(request,'wellcom!! user account was created')

            login(request,user)
            return redirect('profile')
        else:
            messages.error(request, "Username or password incorrect")

    context={
        'page':page,
        'form':form,
    }
    return render(request,'users/logInandRegistertionPage.html',context)

def profile(requset):
    profiles=Profile.objects.all()
    context={
     "profiles":profiles
    }
    return render(requset,'users/profile.html',context)

# @login_required
def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)

    topSkills=profile.skill_set.exclude(descreption__exact='')
    otherSkills=profile.skill_set.filter(descreption='')
    context={
        "profile":profile,
        'topSkills':topSkills,
        'otherSkills':otherSkills,
    }

    return  render(request,'users/userProfile.html',context)


