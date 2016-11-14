import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('remove an alias of a group')

    quiet_fields = {
        'aliasName': _('alias'),
        'groupName': _('group name')
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'aliasName', type=str,
            help=_('the alias alternative to be removed from the group name'))


def main():
    Command().run()
