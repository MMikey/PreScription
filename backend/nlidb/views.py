from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import MedicalStaffSerializer, PatientSerializer, \
    AppointmentSerializer, TreatmentSerializer

from .models import MedicalStaff, Patient, Appointment, Treatment
# Create your views here.

class MedicalStaffView(viewsets.ModelViewSet):
    serializer_class = MedicalStaffSerializer
    queryset = MedicalStaff.objects.all()

class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


