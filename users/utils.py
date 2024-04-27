from . models import Profile,Skill
from django.db.models import Q
from project.models import Project

def searchProfile(request):
    search_query = ''  # we defind the value called search query that in the form of serach anem

    if request.GET.get('search_query'):
         search_query=request.GET.get('search_query')
        # print(f"Search: {search_qurchery}")
    skills=Skill.objects.filter(name__icontains=search_query)

    # profiles=Profile.objects.all()
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)| Q(headline__icontains=search_query)|Q(skill__in=skills))

    return profiles, search_query


