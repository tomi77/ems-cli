import argparse

import pyems


def api_wrapper(parser, uri=None, func=None, name=None, **kwargs):
    try:
        api = pyems.Api(uri)
        api_func = getattr(api, name)
        api_func(**kwargs)
    except pyems.EvoStreamException as e:
        parser.error(e)


def get_parser(description):
    # create the top-level parser
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--uri', help='connection URI', required=True)

    return parser
