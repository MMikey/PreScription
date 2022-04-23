from django.db import models

# Create your models here.

class Translation(models.Model):
    nl_question = models.CharField(
        max_length=1000
        )

    translated_statement = models.CharField(
        max_length=1000,
        editable=False,
        default=''
        )

    sql_statement = models.CharField(
        max_length=100,
        editable=False,
        default='sql statement'
        )

    created = models.DateTimeField(auto_now=True)



