# Generated by Django 3.0.5 on 2020-05-03 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(default=datetime.date(2020, 5, 3)),
        ),
    ]
