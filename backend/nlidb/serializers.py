from rest_framework import serializers
from .models import Staff, Patient, Appointment, Treatment

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('staff_id', 'name', 'salary', 'date_hired', 'working')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('patient_id', 'name', 'DOB', 'NHS_num', 'BMI', 'admitted')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('patient', 'staff', 'date_time', 'treatment', 'description')

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ('treatment_id', 'name', 'description', 'cost')