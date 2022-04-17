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
        return self.remove_stopwords(request)

    def remove_stopwords(self, request):
 
        question = request.data['nl_question']
        question_tokens = word_tokenize(question)

        tokens_without_sw = [word for word in question_tokens if not word in stopwords.words()]

        request.data['nl_question'] = tokens_without_sw

        handler500 = 'error'
        return Response({'nl_question':TreebankWordDetokenizer().detokenize(request.data['nl_question'])})




