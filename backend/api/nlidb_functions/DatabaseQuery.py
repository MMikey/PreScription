from sqlite3 import connect
from nlidb.serializers import StaffSerializer, PatientSerializer, AppointmentSerializer, TreatmentSerializer

from rest_framework.response import Response

from django.db import connection

class DatabaseQuery:
    def __init__(self, sql_query) -> None:
        self.__query__ = sql_query
        print(sql_query)

    def dictfetchall(self, cursor) -> list:
    #
    # Returns a list of rows of table in the form of dicts
    #
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    

    def selectmodel(self,data: list) -> Response:
    #
    # Selects the correct model based on table paramters
    # Data is then serialized and returned as a response object
    #
        if ('patient_id' in data[0]):
            serializer = PatientSerializer(data, many=True)
        elif ('staff_id' in data[0]):
            serializer = StaffSerializer(data, many=True) 
        elif ('treatment_id' in data[0]):
            serializer = TreatmentSerializer(data,many=True)

        return Response(serializer.data)
    
    
    def query(self) -> Response:
        # create connection to database
        with connection.cursor() as cursor:
            cursor.execute(self.__query__)

            data = self.dictfetchall(cursor)
            
            return self.selectmodel(data)

        

