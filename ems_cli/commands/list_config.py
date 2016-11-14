import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('list with all push/pull configurations')

    quiet_fields = {
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
