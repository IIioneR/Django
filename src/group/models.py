from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from faker import Faker
import random

from teacher.models import Teacher


class Group(models.Model):
    name_group = models.CharField(max_length=15, null=False)
    number_of_group = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=False)
    teacher = models.ForeignKey(to=Teacher, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name_group},' \
               f' {self.number_of_group},'

    @classmethod
    def generate_group(cls):
        faker = Faker()
        group = cls(
            name_group=faker.first_name(),
            number_of_group=(random.randint(1, 100)),
        )
        group.save()
