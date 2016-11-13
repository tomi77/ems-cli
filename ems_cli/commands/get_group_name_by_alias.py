import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'returns the group name given the alias name'

    quiet_fields = {
        'groupName': 'group name',
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'aliasName', type=str, help='the group name alias')


def main():
    Command().run()
