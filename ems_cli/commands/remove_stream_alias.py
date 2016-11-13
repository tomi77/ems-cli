from . import BaseCommand


class Command(BaseCommand):
    name = 'remove_stream_alias'

    description = 'removes an alias of a stream'

    quiet_fields = {
        'aliasName': 'alias'
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'aliasName', type=str, help='the alias to delete')


def main():
    Command().run()
