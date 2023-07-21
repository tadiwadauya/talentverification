from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    date_of_registration = models.DateField()
    registration_number = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=50, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    date_started = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    duties = models.TextField()
