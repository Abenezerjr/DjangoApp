from django.shortcuts import render ,redirect
from .models import Project
from .forms import AddProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# def home(request):
#     return render(request,'main.html')

def project(request):

    projects=Project.objects.all()
    conntext={
    'projects':projects
    }
    return render(request,'project/project.html',conntext)

def singleProject(request,pk):
  project=Project.objects.get(id=pk)
  # tags=project.tags.all() We can use in the templet object b/c its many to many relation
  context={
        'project':project,

         # 'tags':tags
    }
  return render(request,'project/singleProject.html',context)

@login_required(login_url='login')
def addProject(request):
    """

    :param request: the addProject form method is post then accept request.post data and it validate the data and send in the database with sission tokne and the database accept the form data and save it
    :return: saved data
    """
    form=AddProjectForm()
    if request.method == "POST":
        form=AddProjectForm(request.POST,request.FILES) #instanc of the new form
        if form.is_valid():
            form.save()
            return redirect("account")
    context={
     'form':form
    }

    return render(request,'project/projectForm.html',context)

@login_required(login_url='login')
def updateProject(request,pk):
    """

    :param request:  from request in the databes wite spacific project
    :param pk:specific project or the project you went to be update
    :return: updated data in the database
    """
    project = Project.objects.get(id=pk)
    form=AddProjectForm(instance=project)

    if request.method=='POST':
        form=AddProjectForm(request.POST,request.FILES,instance=project,)
        if form.is_valid():
            form.save()
            return redirect('account')

    context={
        'form':form
    }
    return render(request,'project/projectForm.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method== 'POST':
        project.delete()
        return redirect('account')

    context={
        'object':project
    }

    return render(request,'project/delete.html',context)

