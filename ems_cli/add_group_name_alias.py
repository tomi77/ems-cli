from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'add_group_name_alias'

    description = 'creates secondary name(s) for group name'

    def _fill_arguments(self, parser):
        parser.add_argument(
            'groupName', type=str, help='the original group name')
        parser.add_argument(
            'aliasName', type=str,
            help='the alias alternative to the group name')


def main():
    Command().run()
