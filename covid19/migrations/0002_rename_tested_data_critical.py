# Generated by Django 4.0 on 2021-12-24 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='tested',
            new_name='critical',
        ),
    ]
