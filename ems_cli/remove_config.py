from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'remove_config'

    description = 'stop the stream and remove the corresponding ' \
                  'configuration entry'

    quiet_fields = {
        'configId': 'config id',
    }

    def __init__(self, subparsers=None, type='id'):
        super(Command, self).__init__(subparsers)
        self.type = type

    def fill_arguments(self):
        if self.type == 'id':
            self.parser.add_argument(
                'id', type=int,
                help='the configId of the configuration that needs to be '
                     'removed')
        else:
            self.parser.add_argument(
                'groupName', type=str,
                help='the name of the group that needs to be removed')
        self.parser.add_argument(
            '--remove-hls-hds-files', type=int, choices=[0, 1],
            dest='removeHlsHdsFiles',
            help='if (1) the folder associated with it will be removed '
                 '(only HLS and HDS stream)')


def main_id():
    Command(type='id').run()


def main_name():
    Command(type='name').run()
