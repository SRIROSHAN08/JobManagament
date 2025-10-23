from django.apps import AppConfig

class JobmanageConfig(AppConfig):
    name = 'jobmanage'  # Use your actual app name here

    def ready(self):
        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    'admin', 'admin@example.com', 'YourStrongPassword123'
                )
        except Exception as e:
            # Log or ignore; most exceptions are DB migration related
            pass
