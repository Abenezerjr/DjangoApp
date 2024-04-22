from django.shortcuts import render
from .models import Profile
# Create your views here.


def profile(requset):
    profiles=Profile.objects.all()
    context={
     "profiles":profiles
    }
    return render(requset,'users/profile.html',context)
