from .utils import BaseCommand


class Command(BaseCommand):
    name = 'list_http_streaming_sessions'

    description = 'all currently active HTTP streaming sessions'

    quiet_fields = {
        'clientIP': 'client ip',
        'sessionId': 'session id',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
