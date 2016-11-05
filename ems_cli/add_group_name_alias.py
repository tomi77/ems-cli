from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'add_group_name_alias'

    description = 'creates secondary name(s) for group name'

    quiet_fields = {
        'groupName': 'group name',
        'aliasName': 'alias name',
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'groupName', type=str, help='the original group name')
        self.parser.add_argument(
            'aliasName', type=str,
            help='the alias alternative to the group name')


def main():
    Command().run()
