from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'add_stream_alias'

    description = 'create secondary name(s) for internal streams'

    def _fill_arguments(self, parser):
        parser.add_argument(
            'localStreamName', type=str,
            help='the original stream name')
        parser.add_argument(
            'aliasName', type=str,
            help='the alias alternative to the local stream name')
        parser.add_argument(
            '--expire-period', type=int, dest='expirePeriod',
            help='the expiration period for this alias')


def main():
    Command().run()
