from django.shortcuts import render
from django.http import HttpResponse

# Create a view called home
def home(request):
    return HttpResponse("Hello, Django!")


