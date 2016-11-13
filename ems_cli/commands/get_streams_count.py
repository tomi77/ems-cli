import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'number of active streams'

    quiet_fields = {
        'count': 'count',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
