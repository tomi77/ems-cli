import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('creates an RTMP ingest point')

    quiet_fields = {
        'privateStreamName': _('private stream name'),
        'publicStreamName': _('public stream name'),
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'privateStreamName', type=str,
            help=_('the name that RTMP Target Stream Names must match'))
        self.parser.add_argument(
            'publicStreamName', type=str,
            help=_('the name that is used to access the stream pushed to the '
                   'privateStreamName'))


def main():
    Command().run()
