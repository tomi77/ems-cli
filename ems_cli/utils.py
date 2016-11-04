import argparse

import pyems


class BaseCommand(object):
    name = None
    description = None

    def __init__(self, subparsers=None):
        if subparsers is not None:
            self.parser = subparsers.add_parser(self.name,
                                                help=self.description)
        else:
            self.parser = argparse.ArgumentParser(description=self.description)
            self.parser.add_argument('--uri', help='connection URI',
                                     required=True)

    def fill_arguments(self):
        self._fill_arguments(self.parser)

    def _fill_arguments(self, parser):
        pass

    def run(self):
        self.fill_arguments()

        args = self.parser.parse_args()
        self.api_wrapper(**args.__dict__)

    def api_wrapper(self, uri=None, **kwargs):
        kwargs = dict([(k, v) for k, v in kwargs.items() if v is not None])
        try:
            api = pyems.Api(uri)
            api_func = getattr(api, self.name)
            api_func(**kwargs)
        except pyems.EvoStreamException as e:
            self.parser.error(e)
