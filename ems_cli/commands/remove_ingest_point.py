import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'remove an RTMP ingest point'

    quiet_fields = {
        'privateStreamName': 'private stream name',
        'publicStreamName': 'public stream name'
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'privateStreamName', type=str,
            help='privateStreamName of ingest point')


def main():
    Command().run()
