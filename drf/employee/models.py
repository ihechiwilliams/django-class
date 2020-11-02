from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_regNo = models.TextField(unique=True)
    employee_name = models.TextField()
    employee_email = models.TextField()
    employee_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

