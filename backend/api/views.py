from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TranslationSerializer
from .models import Translation

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Create your views here.



class TranslationView(viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()

    def post(self, request):
        pass

