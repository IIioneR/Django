from django.core.management.base import BaseCommand
from group.models import Group
from teacher.models import Teacher


class Command(BaseCommand):
    help = 'generate_teachers'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        Group.objects.all().delete()
        teachers = list(Teacher.objects.all())
        count = kwargs['count']
        for _ in range(count):
            Group.generate_group(teachers)

        self.stdout.write(self.style.SUCCESS(f'Created: {count} groups'))
