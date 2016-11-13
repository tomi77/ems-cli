import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'detailed description of all active streams'

    quiet_fields = {
        'uniqueId': 'id',
        'ip': 'ip',
        'name': 'name',
    }

    def fill_arguments(self):
        self.parser.add_argument(
            '--disable-internal-streams', type=int, choices=[0, 1],
            dest='disableInternalStreams',
            help='If (1), internal streams are filtered out from the list')


def main():
    Command().run()
