import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'remove an alias of a group'

    quiet_fields = {
        'aliasName': 'alias',
        'groupName': 'group name'
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'aliasName', type=str,
            help='the alias alternative to be removed from the group name')


def main():
    Command().run()
