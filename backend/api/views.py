from .nlidb.processrequest import ProcessRequest

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import TranslationSerializer
from .models import Translation

from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

import logging
from django.core.exceptions import * 

# Create your views here.

class TranslationView(viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()
    logger = logging.getLogger(__name__)

    def create(self, request):
        question_translator = ProcessRequest(request=request)

        request = question_translator.process()

        obj, created = Translation.objects.get_or_create(
            nl_question=request.data['utterance'],
            translated_statement=request.data['translated_statement'],
            sql_statement=request.data['sql_statement']
        )

        if (not created):
            return Response(request.data)
        else: 
            self.logger.info('Created new question')
            serializer = TranslationSerializer(obj)
            return Response(serializer.data)

    def list(self, request):
        sql_query = Translation.objects.last()

        print(sql_query.__getattribute__('sql_statement'))
        return Translation.objects.raw(sql_query)





