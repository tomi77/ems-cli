import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('terminate a stream')

    quiet_fields = {
        'streamInfo': _('stream info')
    }

    def __init__(self, subparsers=None, type='id'):
        super(Command, self).__init__(subparsers)
        self.type = type

    def fill_arguments(self):
        if self.type == 'id':
            self.parser.add_argument(
                'id', type=int, help=_('the uniqueId of the stream'))
        else:
            self.parser.add_argument(
                'localStreamName', type=str, help=_('the name of the stream'))
        self.parser.add_argument(
            '--permanently', type=int, choices=[0, 1],
            help=_('if (1), the corresponding push/pull configuration will '
                   'also be terminated'))


def main_id():
    Command(type='id').run()


def main_name():
    Command(type='name').run()
