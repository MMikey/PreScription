from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TranslationSerializer
from .models import Translation

# Create your views here.

class TranslationView(viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()
