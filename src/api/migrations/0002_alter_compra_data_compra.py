# Generated by Django 5.1.1 on 2024-09-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='data_compra',
            field=models.DateField(auto_now_add=True),
        ),
    ]
