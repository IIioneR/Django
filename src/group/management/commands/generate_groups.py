from django.core.management.base import BaseCommand
from group.models import Group


class Command(BaseCommand):
    help = 'generate_teachers'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for _ in range(count):
            Group.generate_group()

        self.stdout.write(self.style.SUCCESS(f'Created: {count} groups'))
