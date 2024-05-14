from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getRoutes),
    path('projects/', views.get_projects),
    path('project/<str:pk>/', views.get_project),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # semiple token git using JWT
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refrash Token to usinge time sesstion

]
