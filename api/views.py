from django.http import JsonResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from project.models import Project


@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'/api/projects'},
        {'GET':'api/projects/id'},
        {'GET':'api/users/token'},
        {'GET':'api/user/token/refresh'},

    ]
    return Response(routes)

@api_view(['GET'])
def get_projects(request):
    projects=Project.objects.all()
    serializer = ProjectSerializer(projects,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_project(request,pk):
    project=Project.objects.get(id=pk)
    serializer = ProjectSerializer(project,many=False)

    return Response(serializer.data)