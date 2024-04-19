from django.shortcuts import render

# Create your views here.


def profile(requset):
    context={

    }
    return render(requset,'users/profile.html',context)
