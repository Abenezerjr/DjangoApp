from django.http import JsonResponse


def getRoutes(request):
    routes=[
        {'GET':'/api/projects'},
        {'GET':'api/projects/id'},
        {'GET':'api/users/token'},
        {'GET':'api/user/token/refresh'},

    ]
    return JsonResponse(routes,safe=False)