from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin3@sky.pro',
            first_name='Admin3',
            last_name='Adminov3',
            is_superuser=False,
            is_staff=True,
            is_active=True
        )
        user.set_password('QWErty111')

        user.save()
