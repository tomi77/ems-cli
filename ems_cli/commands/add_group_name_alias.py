import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('creates secondary name(s) for group name')

    quiet_fields = {
        'groupName': _('group name'),
        'aliasName': _('alias name'),
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'groupName', type=str, help=_('the original group name'))
        self.parser.add_argument(
            'aliasName', type=str,
            help=_('the alias alternative to the group name'))


def main():
    Command().run()
