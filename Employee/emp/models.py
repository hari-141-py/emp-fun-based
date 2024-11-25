from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    salary = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name
