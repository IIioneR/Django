# Generated by Django 3.0.5 on 2020-05-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20200506_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
