from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import TranslationSerializer
from .models import Translation
from django.db import transaction



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Create your views here.

class TranslationView(viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()

    def create(self, request):
        request = self.remove_stopwords(request)

        obj, created = self.queryset.get_or_create(
            nl_question=request.data['nl_question'],
            defaults={'sql_statement': 'select *'}
        )
        if(created):
            print('wow')
        
        return request

    def remove_stopwords(self, request):
 
        nl_statement = request.data['nl_question']
        statement_tokens = word_tokenize(nl_statement)

        tokens_without_sw = [word for word in statement_tokens if not word in stopwords.words()]

        request.data['nl_question'] = TreebankWordDetokenizer().detokenize(tokens_without_sw)

        handler500 = 'error'
        return Response(request.data)

    def identify_keywords(self, request):
        nl_statement = request.data['nl_question']
        statement_tokens = word_tokenize(nl_statement)
        




