# Generated by Django 3.0.5 on 2020-05-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20200510_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=50, null=True, unique=True),
        ),
    ]
