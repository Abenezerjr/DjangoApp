from .models import Project
from django.db.models import Q

def searchProject(request):
    search_query=''

    if request.GET.get("search_query"):
        search_query=request.GET.get('search_query')

    # tags=Project.tags.filter(
    #     name__icontains=search_query
    # )

    projects =Project.objects.distinct().filter(

        Q(title__icontains=search_query)|
        Q(owner__name__icontains=search_query)|
        Q(description__icontains=search_query)|
        Q(tags__name__icontains=search_query)

    )

    return projects , search_query