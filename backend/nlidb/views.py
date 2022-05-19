from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import StaffSerializer, PatientSerializer, \
    AppointmentSerializer, TreatmentSerializer

from .models import Staff, Patient, Appointment, Treatment
# Create your views here.

class StaffView(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class AppointmentView(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class TreatmentView(viewsets.ModelViewSet):
    serializer_ckass = TreatmentSerializer
    queryset = Treatment.objects.all()

