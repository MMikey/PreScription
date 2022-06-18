from django.shortcuts import get_object_or_404
from .nlidb_functions.SQLEncoder import SQLEncoder
from .nlidb_functions.DatabaseQuery import DatabaseQuery 

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import TranslationSerializer
from .models import Translation

import logging
from django.core.exceptions import * 

# Create your views here.

class TranslationView(viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()
    logger = logging.getLogger(__name__)
    
    def create(self, request):
        question_translator = SQLEncoder(request)

        request = question_translator.encode_utterance()

        obj, created = Translation.objects.get_or_create(
            utterance=request.data['utterance'],
            sql_query=request.data['sql_query']
        )

        if created:
            self.logger.info('Created new question')

        serializer = TranslationSerializer(obj)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        query = obj.__getattribute__('sql_query')

        
        dbq = DatabaseQuery(query)
        
        results_dict = dbq.query()
        print(results_dict)
        return results_dict
    





