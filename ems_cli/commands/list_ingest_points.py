import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('the currently available Ingest Points')

    quiet_fields = {
        'privateStreamName': _('ingest point'),
        'publicStreamName': _('stream name'),
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
