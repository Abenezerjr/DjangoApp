from django.shortcuts import render
from .models import Project
from .forms import AddProjectForm
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


def addProject(request):
    form=AddProjectForm()
    if request.method == "POST":
        form=AddProjectForm(request.POST)
        if form.is_valid():
            form.save()
    context={
     'form':form
    }

    return render(request,'project/projectForm.html',context)