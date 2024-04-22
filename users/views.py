from django.shortcuts import render
from .models import Profile
# Create your views here.


def profile(requset):
    profiles=Profile.objects.all()
    context={
     "profiles":profiles
    }
    return render(requset,'users/profile.html',context)

def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    context={
        "profile":profile
    }

    return  render(request,'users/userProfile.html',context)
