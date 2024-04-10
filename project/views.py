from django.shortcuts import render

# Create your views here.
ListProject = {
    'hiredive': 'this is a platform that coustomer hire a diveloper',
    'EBC': 'this is a platform that coustomer hire a diveloper',

}
def home(request):
    return render(request,'main.html')

def project(request):
    return render(request,'project/project.html')

def singleProject(request,pk):
    return render(request,'project/singleProject.html')