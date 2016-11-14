import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('number of active streams')

    quiet_fields = {
        'count': _('count'),
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
