from django.urls import path
from .views import app1, goodbye

urlpatterns = [
    path('', app1),
    path('bye/', goodbye)

]
