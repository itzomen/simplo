from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/user/login/',
        'api/user/register/',
        'api/user/logout/',
    ]
    return Response(routes)
