from rest_framework import serializers
from .models import Translation

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ('id', 'nl_question','translated_statement', 'sql_statement', 'created')