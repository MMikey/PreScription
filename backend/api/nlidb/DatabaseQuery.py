from backend.api.nlidb.KWEncoder import KWEncoder

from nlidb.serializers import MedicalStaffSerializer, PatientSerializer, AppointmentSerializer, TreatmentSerializer
from nlidb.models import MedicalStaff, Patient, Appointment, Treatment

from rest_framework.response import Response

class DatabaseQuery():
    def __init__(self, sql_query, table) -> None:
        self.__query__ = sql_query
        self.__table__ = table

    def query(self) -> Response:
        __model = ''
        __serializer = ''
        if (self.__table__ == 'Patient'):
            __model = Patient
            __serializer = PatientSerializer

        obj = __model.objects.raw(self.__query__)
        
        serializer = __serializer(obj)
        return Response(serializer.data) 
