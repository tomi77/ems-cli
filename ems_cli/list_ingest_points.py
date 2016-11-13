from .utils import BaseCommand


class Command(BaseCommand):
    name = 'list_ingest_points'

    description = 'the currently available Ingest Points'

    quiet_fields = {
        'privateStreamName': 'ingest point',
        'publicStreamName': 'stream name',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
