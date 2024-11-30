from django.shortcuts import render
import pandas as pd
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from .models import Company, Employee
from .serializers import Companyserializer, EmployeeSerializer

class FileUploadView(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        print(file)

        try:
            if file.name.endswith('.xlsx') or file.name.endswith('.xls'):
                df = pd.read_excel(file)
            else:
                return Response({"error": "Invalid file format. Only Excel files are allowed."}, status=400)
        except Exception as e:
            return Response({"error": f"Error reading file: {str(e)}"}, status=400)

        companies = {}
        
        for _,row in df.iterrows():
            company_name = row["COMPANY_NAME"]

            if company_name not in companies:
                company, created = Company.objects.get_or_create(company_name = company_name)
                companies[company_name] = company

                employee_data = {
                    "emp_id": row["EMPLOYEE_ID"], 
                    "first_name": row["FIRST_NAME"],
                    "last_name": row["LAST_NAME"],
                    "phone_number": row["PHONE_NUMBER"],
                    "salary": row["SALARY"],
                    "manager_id": row["MANAGER_ID"],
                    "department_id": row["DEPARTMENT_ID"],
                    "company": companies[company_name].id, 
                }

                serializer = EmployeeSerializer(data=employee_data)
            if serializer.is_valid():
                serializer.save()        

        return Response({"message": "Data successfully uploaded."}, status=201)





