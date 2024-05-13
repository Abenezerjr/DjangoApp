from django.urls import  path
from . import  views


urlpatterns=[

    path('',views.profile,name='profile'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logOutPage,name='logout'),
    path('register/',views.registerUser,name='register'),
    path('account/',views.userAccount,name='account'),
    path('edit-account/',views.editAccount,name='editaccount'),
    path('add-skill/',views.addSkil,name='addSkill'),
    path('edit-skill/<str:pk>',views.editSkill,name='editSkill'),
    path('delete-skill/<str:pk>',views.deleteSkill,name='deleteSkill'),
    path('user-profile/<str:pk>',views.userProfile,name='userProfile'),
    path('send-massage/<str:pk>',views.sentMassage,name='sandMassage'),
    path('inbox/',views.Inbox,name='inbox')
]