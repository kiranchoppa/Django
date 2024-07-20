from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=100)

    def __str__(self):
        return self.car_name
