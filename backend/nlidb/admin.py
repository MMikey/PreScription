from django.contrib import admin
from .models import Staff, Patient, Appointment, Treatment
# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id','name', 'salary', 'date_hired', 'is_working')

class PatientsAdmin(admin.ModelAdmin):
    list_display = ('patient_id','name', 'DOB', 'NHS_num', 'BMI', 'admitted')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'staff', 'date_time', 'treatment', 'description')

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatment_id', 'name', 'description', 'cost')


admin.site.register(Staff, StaffAdmin)
admin.site.register(Patient, PatientsAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Treatment, TreatmentAdmin)

