# Generated by Django 3.2.6 on 2021-08-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residential', '0010_alter_residentialdetails_otherrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='residentialdetails',
            name='slug',
            field=models.SlugField(default='wwdh-hbdc', max_length=100),
            preserve_default=False,
        ),
    ]
