import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'removes an alias of a stream'

    quiet_fields = {
        'aliasName': 'alias'
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'aliasName', type=str, help='the alias to delete')


def main():
    Command().run()
