from django.contrib import admin
from .models import MedicalStaff, Patients, Appointments, Treatments
# Register your models here.

class MedicalStaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id','name', 'salary', 'date_hired', 'is_working')

class PatientsAdmin(admin.ModelAdmin):
    list_display = ('patient_id','name', 'DOB', 'NHS_num', 'BMI', 'admitted')

class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'staff', 'description', 'date_time')

class TreatmentsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'staff', 'cost', 'description')


admin.site.register(MedicalStaff, MedicalStaffAdmin)
admin.site.register(Patients, PatientsAdmin)
admin.site.register(Appointments, AppointmentsAdmin)
admin.site.register(Treatments, TreatmentsAdmin)

