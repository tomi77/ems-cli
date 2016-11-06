from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'get_streams_count'

    description = 'number of active streams'

    quiet_fields = {
        'streamCount': 'count',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
