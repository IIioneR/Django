# Generated by Django 3.0.5 on 2020-05-06 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20200506_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(default=380, max_length=15, unique=True),
        ),
    ]
