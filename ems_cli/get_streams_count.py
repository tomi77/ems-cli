from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'get_streams_count'

    description = 'number of active streams'

    quiet_fields = {
        'count': 'count',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
