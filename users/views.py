from django.shortcuts import render ,  redirect
from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile ,Skill
from django.contrib import messages
# from django.db.models import Q
from .utils import searchProfile
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm ,EditAccountForm ,SkillForm
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
            messages.success(request,'wellcome!! user account was created')

            login(request,user)
            return redirect('profile')
        else:
            messages.error(request, "Username or password incorrect")

    context={
        'page':page,
        'form':form,
    }
    return render(request,'users/logInandRegistertionPage.html',context)

def profile(request):
    profiles , search_query =searchProfile(request)
    # search_query='' # we defind the value called search query that in the form of serach anem
    #
    # if requset.GET.get('search_query'): # we cheack if that is a get requsest
    #     search_query=requset.GET.get('search_query')
    #     # print(f"Search: {search_query}")
    #
    # skills=Skill.objects.filter(name__icontains=search_query)
    #
    # # profiles=Profile.objects.all()
    # profiles = Profile.objects.distinct().filter(
    #     Q(name__icontains=search_query)| Q(headline__icontains=search_query)|Q(skill__in=skills))
    context={
     "profiles":profiles,
     "search_query":search_query,
    }
    return render(request,'users/profile.html',context)

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

def userAccount(request):
    profile=request.user.profile
    context={
        "profile":profile

    }
    return render(request,'users/userAccount.html',context)

def editAccount(request):
    """

    :param request:
    :return: form with instance of profile
    """
    profile=request.user.profile # get login user
    form=EditAccountForm(instance=profile)  # get editform with instance of profile meas that the user detali befor
    if request.method == 'POST': # chek request.PoSt method is send? or the user make some change ?
        form=EditAccountForm(request.POST,request.FILES,instance=profile) #yes ? add in the for is valid
        if form.is_valid(): # if it valid
            form.save() # save in to the databesa
            return redirect('account') # send to the user account

    context={
        'form':form
    }

    return render(request,'project/projectForm.html',context)


def addSkil(request):
    profile = request.user.profile# get profile
    form=SkillForm() # get skillform
    if request.method == 'POST': # check the requset is post
        form=SkillForm(request.POST) # if it post add the user requset in the form
        if form.is_valid(): # its valied
            skill=form.save(commit=False) # save the form in the skile varible not in the database
            skill.owner=profile # check the profile is the owner
            skill.save() # save that owner
            return  redirect('account')

    context={
        'form':form
    }

    return render(request,'project/projectForm.html',context)


def editSkill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    form=SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            # ask=form.save(commit=False)
            # ask.owner=profile
            skill.save()
            return redirect('account')

    context={
        'form':form
    }


    return render(request,'project/projectForm.html',context)

def deleteSkill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        return redirect('account')


    context= {
        'object':skill
    }

    return render(request ,'project/delete.html',context)