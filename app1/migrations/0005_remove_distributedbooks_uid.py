# Generated by Django 5.0.4 on 2024-05-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_distributedbooks_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributedbooks',
            name='uid',
        ),
    ]
