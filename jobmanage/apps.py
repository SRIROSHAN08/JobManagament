from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.utils import OperationalError

class JobmanageConfig(AppConfig):
    name = 'jobmanage'  # use your actual app name here

    def ready(self):
        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('roshan', 'sriroshanro8@gmail.com', 'Roshan@08')
        except OperationalError:
            pass
