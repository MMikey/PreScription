from backend.api.nlidb.KWEncoder import KWEncoder
from nlidb.serializers import MedicalStaffSerializer, PatientSerializer, AppointmentSerializer, TreatmentSerializer
from nlidb.models import MedicalStaff, Patient, Appointment, Treatment

from rest_framework.response import Response

class Querier():
    def __init__(self) -> None:
        pass

    