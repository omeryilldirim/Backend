from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=64, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Personnel(models.Model):
    GENDERS = (('F', 'Female'),('M', 'Male'),('0', 'Prefer Not To Say'))

    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    gender = models.CharField(max_length=16, choices=GENDERS)
    age = models.PositiveIntegerField()
    title = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    salary = models.PositiveIntegerField()
    started = models.DateField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_personnel')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.surname}'