from django.urls import path
from .views import (
    UserLoginView,
    UserLogoutView,
    UserCreateView
)

# 'user/' ->
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('register/', UserCreateView.as_view(), name='user_register')
,]