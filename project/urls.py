from django.urls import path
from . import  views

urlpatterns=[
path("",views.project,name='projects'),
# path("home/",views.home),
path("single-project/<str:pk>",views.singleProject,name='project'),

]

