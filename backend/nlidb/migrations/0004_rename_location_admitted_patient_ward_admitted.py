# Generated by Django 3.2.12 on 2022-05-14 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nlidb', '0003_auto_20220421_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='location_admitted',
            new_name='ward_admitted',
        ),
    ]