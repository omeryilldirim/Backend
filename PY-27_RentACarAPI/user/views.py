
from .serializers import (
    User, UserSerializer,
)

# --------------------------------
# UserCreateView -> Only CreateUser for permissions.AllowAny
# --------------------------------
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

class UserCreateView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    # override create() to create Token and login automatically
    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # no matter what user send, these fields will be set. avoid user to set himself superuser
        serializer.validated_data['is_active'] = True
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_superuser'] = False
        # <--- User.save() & Token.create() --->
        user = serializer.save()
        data = serializer.data
        token = Token.objects.create(user=user)
        data['key'] = token.key
        # </--->
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

# --------------------------------
# UserViewSet
# --------------------------------
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAdminUser

class UserView(ModelViewSet):
    # this is for staff to see all users except superusers
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser] # default : IsAdminUser