from django.urls import path
from . import  views

urlpatterns=[
path("project/",views.project),
path("home/",views.home),
path("single-project/<str:pk>",views.singleProject),

]

