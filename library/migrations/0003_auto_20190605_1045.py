# Generated by Django 2.2 on 2019-06-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20190605_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='date_returned',
            field=models.DateField(blank=True, null=True),
        ),
    ]
