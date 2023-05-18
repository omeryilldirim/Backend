from django.urls import path, include
from rest_framework import routers
from .views import UserView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": "Logout success"}, status=status.HTTP_200_OK)


router = routers.DefaultRouter()
router.register('', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', obtain_auth_token),
    path('logout', logout),
]