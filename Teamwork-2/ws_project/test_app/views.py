from django.shortcuts import render
from django.http import HttpResponse

# Create a view called home
def home(request):
    return HttpResponse("<h1 style='color:red'>Hello, Django!</h1>")


