from .utils import BaseCommand


class Command(BaseCommand):
    name = 'list_stream_aliases'

    description = 'a complete list of aliases'

    quiet_fields = {
        'aliasName': 'alias name',
        'localStreamName': 'stream name',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
