import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('invalidates all stream aliases')

    def fill_arguments(self):
        pass

    def format_quiet_msg(self, data):
        return self.format_verbose_msg(data)

    @staticmethod
    def format_verbose_msg(data):
        return _('All aliases are flushed')


def main():
    Command().run()
