# Generated by Django 3.2.6 on 2021-08-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residential', '0008_residentialdetails_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residentialdetails',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
