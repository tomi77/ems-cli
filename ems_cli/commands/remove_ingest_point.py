import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('remove an RTMP ingest point')

    quiet_fields = {
        'privateStreamName': _('private stream name'),
        'publicStreamName': _('public stream name')
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'privateStreamName', type=str,
            help=_('privateStreamName of ingest point'))


def main():
    Command().run()
