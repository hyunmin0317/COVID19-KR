# Generated by Django 3.2.5 on 2021-07-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('confirmed', models.IntegerField()),
                ('death', models.IntegerField()),
                ('released', models.IntegerField()),
                ('tested', models.IntegerField()),
                ('today', models.IntegerField()),
            ],
        ),
    ]
