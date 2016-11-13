import argparse
import json
import sys

import pyems


class BaseCommand(object):
    name = None
    description = None
    quiet_fields = {}

    def __init__(self, subparsers=None):
        if subparsers is not None:
            self.parser = subparsers.add_parser(self.name,
                                                help=self.description)
        else:
            self.parser = argparse.ArgumentParser(description=self.description)
            self.parser.add_argument('--connection-uri', help='connection URI',
                                     dest="connection_uri", required=True)
            self.parser.add_argument('-v', '--verbose', action='store_true',
                                     help='verbose mode')

    def fill_arguments(self):
        raise NotImplementedError()

    def format_quiet_msg(self, data):
        if isinstance(data, dict):
            data = [data]

        return '\n\n'.join(['\n'.join(['%s: %s' % (desc, row[name])
                                       for name, desc
                                       in self.quiet_fields.items()])
                            for row in data])

    @staticmethod
    def format_verbose_msg(data):
        return json.dumps(data, indent=2)

    def run(self):
        self.fill_arguments()

        args = self.parser.parse_args()
        self.api_wrapper(**args.__dict__)

    def api_wrapper(self, connection_uri=None, verbose=False, **kwargs):
        kwargs = dict([(k, v) for k, v in kwargs.items() if v is not None])
        try:
            api = pyems.Api(connection_uri)
            api_func = getattr(api, self.name)
            data = api_func(**kwargs)
        except pyems.EvoStreamException as e:
            sys.stderr.write('%s\n' % e)
        else:
            msg = self.format_verbose_msg(data) \
                if verbose else self.format_quiet_msg(data)
            sys.stdout.write('%s\n' % msg)
