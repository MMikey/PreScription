from django.contrib import admin
from .models import Translation

# Register your models here.

class TranslationAdmin(admin.ModelAdmin):
    list_display = ('nl_question','translated_statement', 'sql_statement', 'created')


admin.site.register(Translation, TranslationAdmin)