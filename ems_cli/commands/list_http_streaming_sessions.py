import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'all currently active HTTP streaming sessions'

    quiet_fields = {
        'clientIP': 'client ip',
        'sessionId': 'session id',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
