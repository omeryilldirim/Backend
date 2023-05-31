from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    

class Personnel(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('N', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    TITLE = (
        ('S', 'Senior'),
        ('M', 'Mid-senior'),
        ('J', 'Junior'),
    )
    title = models.CharField(max_length=1, choices=TITLE)
    salary = models.IntegerField()
    started = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='personnel')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    