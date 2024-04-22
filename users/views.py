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

    topSkills=profile.skill_set.exclude(descreption__exact='')
    otherSkills=profile.skill_set.filter(descreption='')
    context={
        "profile":profile,
        'topSkills':topSkills,
        'otherSkills':otherSkills,
    }

    return  render(request,'users/userProfile.html',context)
