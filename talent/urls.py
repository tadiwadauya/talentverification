from django.urls import path
from .views import CompanyAPIView, EmployeeAPIView
from talent.views import get_data

urlpatterns = [
    path('api/company/', CompanyAPIView.as_view(), name='company-api'),
    path('api/employee/', EmployeeAPIView.as_view(), name='employee-api'),
    path('api/employee/<int:employee_id>/', EmployeeAPIView.as_view(), name='employee-detail-api'),
    path('api/data/', get_data, name='get_data'),
    # Other URL patterns for your project...
]