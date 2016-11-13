from . import BaseCommand


class Command(BaseCommand):
    name = 'list_streams_ids'

    description = 'a list of IDs for every active stream'

    def fill_arguments(self):
        pass

    def format_quiet_msg(self, data):
        return data


def main():
    Command().run()
