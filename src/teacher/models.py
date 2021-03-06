from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, default=380 - 000 - 000 - 000, unique=True)

    def __str__(self):
        return f'{self.first_name},' \
               f' {self.last_name},' \
               f' {self.email},' \
               f' {self.phone_number}'

    @classmethod
    def generate_teacher(cls):
        faker = Faker()
        teacher = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=faker.phone_number(),
        )
        teacher.save()
