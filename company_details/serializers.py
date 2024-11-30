from rest_framework import serializers
from .models import Company, Employee


class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'company_name']


class EmployeeSerializer(serializers.ModelSerializer):

    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())  

    class Meta:
        model = Employee
        fields = ['emp_id', 'first_name', 'last_name', 'phone_number', 'salary', 'manager_id', 'department_id', 'company']

