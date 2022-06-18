import json

from rest_framework import viewsets
from rest_framework.response import Response
from nlidb.models import Staff, Patient, Appointment, Treatment


def TableDataLoader():
    def save_to_file(self, table_data:dict  ):
        open('table_data.json', 'x')
        with open('table_data.json', 'w') as fp:
            json.dump(table_data, fp)


    def get_tbl_names(self, models):
        table_data = {}
        for m in models:
            table_data[m.__meta.db_table] = []

        return table_data

    def get_tbl_data(self, models):
        table_data = self.get_tbl_names(models)

        i = 0
        for x in table_data:
            table_data[x] = models[i].__meta.get_fields()
            i += 1

        return table_data

    def load_table_data(self, request):
        models = [Staff, Patient, Appointment, Treatment]
        self.get_tbl_names(models)
        td = self.get_tbl_data(models)

        return Response(json.dumps(td))
