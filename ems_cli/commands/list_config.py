import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'list with all push/pull configurations'

    quiet_fields = {
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
