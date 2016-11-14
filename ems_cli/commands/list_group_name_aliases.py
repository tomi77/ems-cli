import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('a complete list of group name aliases')

    quiet_fields = {
        'aliasName': _('alias name'),
        'groupName': _('group name'),
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
