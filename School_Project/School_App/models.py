from django.db import models
from datetime import datetime

GENDER_CHOICES = [('Male','Male'),('Female','Female')]
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Purpose(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,
                            choices= GENDER_CHOICES)
    phone = models.IntegerField()
    mail = models.EmailField(unique=True)
    address = models.TextField(max_length=700)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)
    materials_provided = models.CharField(max_length=150, null=True)

    def __str__(self) -> str:
        return self.name
    