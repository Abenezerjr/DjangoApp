from django.urls import  path
from . import  views


urlpatterns=[

    path('',views.profile,name='profile'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logOutPage,name='logout'),
    path('user-profile/<str:pk>',views.userProfile,name='userProfile'),
]