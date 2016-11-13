from .utils import BaseCommand


class Command(BaseCommand):
    name = 'get_config_info'

    description = 'information of the stream by the configId'

    quiet_fields = {
        'configId': 'id',
        'localStreamName': 'local stream name',
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'id', type=int, help='the configId of the configuration')


def main():
    Command().run()
