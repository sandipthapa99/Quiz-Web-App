from django.apps import AppConfig


# signals to create profile whenever user is created
class ParticipantsConfig(AppConfig):
    name = 'participants'

    def ready(self):
        import participants.signals
