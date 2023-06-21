from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def home(request):
    return HttpResponse('<h1 style="color:red">Hello World!</h1>')


def student(request):
    context = {
        'first_name':'rafe',
        'my_list': [2020, 2021, 2022],
        'book_name':'lord of the rings'
        }
    return render(request, 'home/home.html', context)


def student_detail(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'home/student_detail.html', context)


from .forms import StudentForm
from django.shortcuts import redirect

def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'home/student_add.html', context)



from django.views.generic import CreateView
from django.urls import reverse_lazy

class StudentAddView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list')
    # default template : 'home/student_form.html' ama yeni bir html oluşturmadan farklı isimdeki template kullanmak için template_name attribute eklenir.
    template_name = 'home/student_add.html'