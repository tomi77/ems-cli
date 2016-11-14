import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('returns the group name given the alias name')

    quiet_fields = {
        'groupName': _('group name'),
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'aliasName', type=str, help=_('the group name alias'))


def main():
    Command().run()
