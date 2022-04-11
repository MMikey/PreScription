from rest_framework import serializers
from .models import Translation

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ('id', 'nl_question', 'sql_statement', 'created')