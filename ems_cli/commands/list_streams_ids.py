import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('a list of IDs for every active stream')

    def fill_arguments(self):
        pass

    def format_quiet_msg(self, data):
        return data


def main():
    Command().run()
