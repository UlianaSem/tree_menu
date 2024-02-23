from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            User.objects.get(username='admin')
        except User.DoesNotExist:
            User.objects.create_user(
                username='admin',
                password='admin',
                is_staff=True,
                is_superuser=True,
            )
