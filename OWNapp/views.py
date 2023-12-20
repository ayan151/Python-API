from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication

# Create your views here.
class EmployeeListView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[BasicAuthentication]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
