import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'invalidates all stream aliases'

    def fill_arguments(self):
        pass

    def format_quiet_msg(self, data):
        return self.format_verbose_msg(data)

    @staticmethod
    def format_verbose_msg(data):
        return 'All aliases are flushed'


def main():
    Command().run()
