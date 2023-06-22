
class FixView:
    template_name = 'user/user_form.html'
    next_page = 'user_login'

# --------------------------------------------------
# User Login-Logout
# --------------------------------------------------
from typing import Any
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse

class UserLoginView(FixView, LoginView):
    pass


class UserLogoutView(FixView, LogoutView):
    pass


# --------------------------------------------------
# User Registration
# --------------------------------------------------
from django.contrib.auth.forms import UserCreationForm
# from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class UserCreateView(FixView, CreateView):
    form_class = UserCreationForm
    # success_url = '/user/login/'
    success_url = reverse_lazy(FixView.next_page)

    # Login after registration:
    def get_success_url(self):
        from django.contrib.auth import login
        login(self.request, self.object)
        return super().get_success_url()