# Generated by Django 4.1.5 on 2023-03-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='gender',
            field=models.CharField(max_length=100),
        ),
    ]