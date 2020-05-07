from django.core.management.base import BaseCommand
from student.models import Student


class Command(BaseCommand):
    help = 'generate_students'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for _ in range(count):
            Student.generate_student()

        self.stdout.write(self.style.SUCCESS(f'Created: {count} students'))
