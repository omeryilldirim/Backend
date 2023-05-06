from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    engine = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}  ({self.year})  Reg_date: {self.registration_date}'