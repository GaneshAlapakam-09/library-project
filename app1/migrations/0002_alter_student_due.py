# Generated by Django 5.0.4 on 2024-05-03 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='due',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
