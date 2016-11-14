import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('removes an alias of a stream')

    quiet_fields = {
        'aliasName': _('alias')
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'aliasName', type=str, help=_('the alias to delete'))


def main():
    Command().run()
