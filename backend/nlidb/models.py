from django.db import models

# Create your models here.

class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True, default=0)

    name = models.CharField(max_length=50)
    salary = models.FloatField()
    date_hired = models.DateField('date hired')
    working = models.BooleanField()

class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True, default=0)

    name = models.CharField(max_length=50)
    DOB = models.DateField('date of birth')
    NHS_num = models.IntegerField()
    BMI = models.IntegerField()
    admitted = models.BooleanField()


class Treatment(models.Model):
    treatment_id = models.IntegerField(primary_key=True, default=0)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cost = models.FloatField()

class Appointment(models.Model):
    class Meta:
        unique_together = (('patient', 'staff', 'date_time'),)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, primary_key=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    treatment = models.ForeignKey(Treatment, blank=True, null=True,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)