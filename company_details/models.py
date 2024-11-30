from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=225)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    emp_id = models.IntegerField(max_length=5)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length= 20)
    phone_number = models.CharField(max_length= 20)
    salary = models.FloatField(max_length=10)
    manager_id = models.IntegerField(max_length=5)
    department_id = models.IntegerField(max_length=5)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

