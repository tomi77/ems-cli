import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('information of the stream by the configId')

    quiet_fields = {
        'configId': _('id'),
        'localStreamName': _('local stream name'),
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'id', type=int, help=_('the configId of the configuration'))


def main():
    Command().run()
