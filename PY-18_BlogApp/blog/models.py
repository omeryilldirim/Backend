from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
