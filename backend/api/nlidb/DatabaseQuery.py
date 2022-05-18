from nlidb.serializers import MedicalStaffSerializer, PatientSerializer, AppointmentSerializer, TreatmentSerializer
from nlidb.models import MedicalStaff, Patient, Appointment, Treatment

from rest_framework.response import Response

from django.db import connection, transaction

class DatabaseQuery:
    def __init__(self, sql_query) -> None:
        self.__query__ = sql_query

    def query(self) -> Response:
        with connection.cursor() as cursor:
            cursor.execute(self.__query__)
            row = cursor.fetchone()
        
