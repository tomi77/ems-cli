import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'the currently available Ingest Points'

    quiet_fields = {
        'privateStreamName': 'ingest point',
        'publicStreamName': 'stream name',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
