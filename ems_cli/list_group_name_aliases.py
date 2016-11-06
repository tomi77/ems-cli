from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'list_group_name_aliases'

    description = 'a complete list of group name aliases'

    quiet_fields = {
        'aliasName': 'alias name',
        'groupName': 'group name',
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
