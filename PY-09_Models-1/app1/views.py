from django.http import HttpResponse


# Create your views here.
def app1(request):
    return HttpResponse('<h2>This is the app page</h2>')
def goodbye(request):
    return HttpResponse('<h2>Goodbye!</h2>')