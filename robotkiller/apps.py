from django.apps import AppConfig


class RobotkillerConfig(AppConfig):
    name = 'robotkiller'
    verbose_name = 'Robotkiller kill frequency IP'
    def ready(self):
        import robotkiller.signals
