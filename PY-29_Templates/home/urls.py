from django.contrib import admin
from django.urls import path, include
from .views import home, student, student_detail

urlpatterns = [
    path('', home),
    path('student/', student),
    path('detail/', student_detail)
]
