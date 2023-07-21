from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
from talent.models import Company, Employee

from .models import Company, Employee, EmployeeHistory
from .serializers import CompanySerializer, EmployeeSerializer, EmployeeHistorySerializer 

class CompanyAPIView(APIView):
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeAPIView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, employee_id):
        employee = get_object_or_404(Employee, id=employee_id)
        serializer = EmployeeSerializer(employee)
        history = EmployeeHistory.objects.filter(employee=employee).order_by('-timestamp')
        history_serializer = EmployeeHistorySerializer(history, many=True)
        return Response({
            'employee': serializer.data,
            'history': history_serializer.data
        })

    def put(self, request, employee_id):
        employee = get_object_or_404(Employee, id=employee_id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_data(request):
        companies = Company.objects.all()
        employees = Employee.objects.all()
        data = {
            'companies': list(companies.values()),
            'employees': list(employees.values()),
    }
        return JsonResponse(data)