import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('create secondary name(s) for internal streams')

    quiet_fields = {
        'localStreamName': _('local stream name'),
        'aliasName': _('alias name'),
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'localStreamName', type=str,
            help=_('the original stream name'))
        self.parser.add_argument(
            'aliasName', type=str,
            help=_('the alias alternative to the local stream name'))
        self.parser.add_argument(
            '--expire-period', type=int, dest='expirePeriod',
            help=_('the expiration period for this alias'))


def main():
    Command().run()
