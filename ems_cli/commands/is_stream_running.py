import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'checks a specific stream if it is running or not'

    quiet_fields = {
        'Running': 'running?',
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


def main_id():
    Command(type='id').run()


def main_name():
    Command(type='name').run()
