from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import TranslationSerializer
from django.db import IntegrityError, transaction

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
        request = self.remove_stopwords(request)
        request = self.identify_keywords(request)

        obj, created = self.queryset.get_or_create(
            nl_question=request.data['nl_question'],
            defaults={'sql_statement': ''}  
        )
        if (created):
            self.logger.info('Created new question')
            return Response(request.data)
        else: 
            serializer = TranslationSerializer(obj)
            return Response(serializer.data)

    def remove_stopwords(self, request):
 
        nl_statement = request.data['nl_question']
        statement_tokens = word_tokenize(nl_statement)

        tokens_without_sw = [word for word in statement_tokens if not word in stopwords.words()]

        request.data['translated_statement'] = TreebankWordDetokenizer().detokenize(tokens_without_sw)

        handler500 = 'error'
        return Response(request.data)

    def identify_keywords(self, request):
        nl_statement = request.data['nl_question']
        statement_tokens = word_tokenize(nl_statement)
        
        corpus_root  = './api/keywords'

        filelists = PlaintextCorpusReader(corpus_root, '.*')

        filelists.fileids()

        table_names = filelists.words('table_names.txt')

        kw_tokens = [word for word in statement_tokens if word in table_names]

        request.data['translated_st'] = TreebankWordDetokenizer().detokenize(kw_tokens)

        return Response(request.data)
        
        




