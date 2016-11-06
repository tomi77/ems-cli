from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'list_config'

    description = 'list with all push/pull configurations'

    quiet_fields = {
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
