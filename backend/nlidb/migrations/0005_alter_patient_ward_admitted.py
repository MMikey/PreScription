# Generated by Django 3.2.12 on 2022-05-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlidb', '0004_rename_location_admitted_patient_ward_admitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ward_admitted',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]