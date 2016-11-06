from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'get_group_name_by_alias'

    description = 'returns the group name given the alias name'

    quiet_fields = {
        'groupName': 'group name',
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'aliasName', type=str, help='the group name alias')


def main():
    Command().run()
