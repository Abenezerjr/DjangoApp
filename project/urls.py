from django.urls import path
from . import  views

urlpatterns=[
path("",views.project,name='projects'),
# path("home/",views.home),
path("single-project/<str:pk>/",views.singleProject,name='project'),
path("addproject/",views.addProject,name='addproject'),
path("update-project/<str:pk>/",views.updateProject,name='update'),
path("delete-project/<str:pk>/",views.deleteProject,name='delete-project'),

]

