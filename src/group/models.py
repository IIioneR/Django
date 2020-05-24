from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from faker import Faker
import random

from teacher.models import Teacher


class ClassRoom(models.Model):
    name = models.CharField(max_length=64)
    floor = models.SmallIntegerField(max_length=128, null=None)

    def __str__(self):
        return f'{self.name},' \
               f' {self.floor},'

    @classmethod
    def generate_classroom(cls):
        faker = Faker()
        classroom = cls(
            name=faker.last_name(),
            floor=(random.randint(1, 100)),
        )
        classroom.save()


class Group(models.Model):
    name_group = models.CharField(max_length=15, null=False)
    number_of_group = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=False)
    teacher = models.ForeignKey(to=Teacher, null=True, on_delete=models.SET_NULL, related_name='groups')
    classroom = models.ManyToManyField(to=ClassRoom, null=True, related_name='groups')

    def __str__(self):
        return f'{self.name_group},' \
               f' {self.number_of_group},'

    @classmethod
    def generate_group(cls, teachers=None):
        if teachers is None:
            teachers = list(Teacher.objects.all())
        faker = Faker()
        group = cls(
            name_group=faker.first_name(),
            number_of_group=(random.randint(1, 100)),
            teacher=random.choice(teachers)
        )
        group.save()
