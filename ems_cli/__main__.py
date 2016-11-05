import ems_cli
from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    description = 'EMS cli'

    def fill_arguments(self):
        subparsers = self.parser.add_subparsers(help='command')

        ems_cli.add_group_name_alias.Command(subparsers).fill_arguments()
        ems_cli.add_stream_alias.Command(subparsers).fill_arguments()
        ems_cli.create_dash_stream.Command(subparsers).fill_arguments()
        ems_cli.create_hds_stream.Command(subparsers).fill_arguments()
        ems_cli.create_hls_stream.Command(subparsers).fill_arguments()


def main():
    Command().run()
