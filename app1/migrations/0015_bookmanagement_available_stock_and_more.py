# Generated by Django 5.0.4 on 2024-05-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_bookmanagement_stock_delete_distributedbooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmanagement',
            name='available_stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bookmanagement',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
