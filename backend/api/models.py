from django.db import models

# Create your models here.

class Translation(models.Model):
    utterance = models.CharField(
        max_length=1000
        )

    sql_query = models.CharField(
        max_length=100,
        editable=False,
        default=''
        )

    created = models.DateTimeField(auto_now=True)



