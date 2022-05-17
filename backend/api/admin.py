from django.contrib import admin
from .models import Translation

# Register your models here.

class TranslationAdmin(admin.ModelAdmin):
    list_display = ('utterance', 'sql_query', 'created')


admin.site.register(Translation, TranslationAdmin)