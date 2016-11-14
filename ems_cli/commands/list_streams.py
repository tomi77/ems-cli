import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('detailed description of all active streams')

    quiet_fields = {
        'uniqueId': _('id'),
        'ip': _('ip'),
        'name': _('name'),
    }

    def fill_arguments(self):
        self.parser.add_argument(
            '--disable-internal-streams', type=int, choices=[0, 1],
            dest='disableInternalStreams',
            help=_('If (1), internal streams are filtered out from the list'))


def main():
    Command().run()
