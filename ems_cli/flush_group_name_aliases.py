from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'flush_group_name_aliases'

    description = 'invalidates all group name aliases'

    def fill_arguments(self):
        pass

    def format_quiet_msg(self, data):
        return self.format_verbose_msg(data)

    @staticmethod
    def format_verbose_msg(data):
        return 'All group name aliases are flushed'


def main():
    Command().run()
