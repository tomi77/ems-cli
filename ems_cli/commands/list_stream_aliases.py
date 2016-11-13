import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'a complete list of aliases'

    quiet_fields = {
        'aliasName': 'alias name',
        'localStreamName': 'stream name',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
