from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'shutdown_stream'

    description = 'Terminate a stream'

    quiet_fields = {
        'aliasName': 'alias'
    }

    def __init__(self, subparsers=None, type='id'):
        super(Command, self).__init__(subparsers)
        self.type = type

    def fill_arguments(self):
        if self.type == 'id':
            self.parser.add_argument(
                'id', type=int, help='the uniqueId of the stream')
        else:
            self.parser.add_argument(
                'localStreamName', type=str, help='the name of the stream')
        self.parser.add_argument(
            '--permanently', type=int, choices=[0, 1],
            help='if (1), the corresponding push/pull configuration will '
                 'also be terminated')


def main_id():
    Command(type='id').run()


def main_name():
    Command(type='name').run()
