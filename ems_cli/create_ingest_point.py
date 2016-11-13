from .utils import BaseCommand


class Command(BaseCommand):
    name = 'create_ingest_point'

    description = 'creates an RTMP ingest point'

    quiet_fields = {
        'privateStreamName': 'private stream name',
        'publicStreamName': 'public stream name',
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'privateStreamName', type=str,
            help='the name that RTMP Target Stream Names must match')
        self.parser.add_argument(
            'publicStreamName', type=str,
            help='the name that is used to access the stream pushed to the '
                 'privateStreamName')


def main():
    Command().run()
