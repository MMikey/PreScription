from django.db import models

# Create your models here.

class MedicalStaff(models.Model):
    staff_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=50)
    salary = models.FloatField()
    date_hired = models.DateField('date hired')
    is_working = models.BooleanField()

class Patients(models.Model):
    patient_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=50)
    DOB = models.DateField('date of birth')
    NHS_num = models.IntegerField()
    BMI = models.IntegerField()
    admitted = models.BooleanField()
    location_admitted = models.CharField(max_length=200)

class Appointments(models.Model):
    class Meta:
        unique_together = (('patient', 'staff'),)

    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, primary_key=True)
    staff = models.ForeignKey(MedicalStaff, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date_time = models.DateTimeField()

class Treatments(models.Model):
    class Meta:
        unique_together = (('patient', 'staff'),)

    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, primary_key=True)
    staff = models.ForeignKey(MedicalStaff, on_delete=models.CASCADE)
    cost = models.FloatField()
    description = models.CharField(max_length=200)