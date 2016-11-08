from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'remove_ingest_point'

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
