from django.shortcuts import render

# Create your views here.
ListProject = [
    {
    'id': '1',
    'title': 'EBC',
    'discription':'ethiopan backend developers'
},
    {
    'id': '2',
    'title': 'HireDev',
    'discription':'this is a platform that coustomer hire a diveloper'
},
    {
    'id': '3',
    'title': 'blog',
    'discription':'blog page personal page'
}

]


# def home(request):
#     return render(request,'main.html')

def project(request):
    msg='hello im in from project'
    number=30
    conntext={
        'listofproject':ListProject,
        'msg':msg,
        'number':number,
    }
    return render(request,'project/project.html',conntext)

def singleProject(request,pk):
    projectObj=None
    for i in ListProject:
        if i['id'] ==pk:
            projectObj=i
    context={
        'projectObj':projectObj
    }
    return render(request,'project/singleProject.html',context)