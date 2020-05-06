import datetime
from django.db import models

# Create your models here.
from faker import Faker


class Student(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, unique=True)
    birthday = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(max_length=15, default=380000000000, unique=True)

    def __str__(self):
        return f' {self.first_name},' \
               f' {self.last_name},' \
               f' {self.birthday},' \
               f' {self.email},' \
               f' {self.phone_number}'

    @classmethod
    def generate_student(cls):
        faker = Faker()
        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=faker.phone_number(),
        )

        student.save()