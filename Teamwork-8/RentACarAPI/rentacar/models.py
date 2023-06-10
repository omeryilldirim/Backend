from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=64)
    address = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    GEAR = (('M', 'Manual' ), ('A','Automatic'))

    plate_number = models.CharField(max_length=10)
    brand = models.CharField(max_length=32)
    model  = models.CharField(max_length=32)
    year = models.PositiveSmallIntegerField()
    gear = models.CharField(max_length=16, choices=GEAR)
    rent_per_day = models.PositiveSmallIntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} / {self.model} - {self.plate_number}"
    

class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.customer} --> {self.car}"
    
    def total_price(self):
        return (self.end_date - self.start_date).days * self.car.rent_per_day
    

class Query(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    available_cars = models.ManyToManyField(Car)

    def __str__(self):
        return f"{self.start_date} --> {self.end_date}"
