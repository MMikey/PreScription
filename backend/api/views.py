from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import TranslationSerializer
from .models import Translation

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Create your views here.

class TranslationView(viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()

    def create():

        
    @action(detail=True, methods=['post'])
    def remove_stopwords(self, request):
 
        question = request.data['nl_question']
        question_tokens = word_tokenize(question)

        tokens_without_sw = [word for word in question_tokens if not word in stopwords.words()]

        request.data['nl_question'] = tokens_without_sw

        return Response({'status':'stop words removed'})




