import argparse

from ems_cli.utils import api_wrapper, get_parser


DESCRIPTION = 'create secondary name(s) for internal streams'
NAME = 'add_stream_alias'


def subparser(parser):
    """create the parser for the "add_stream_alias" command"""
    if not isinstance(parser, argparse._SubParsersAction):
        subparser = parser
    else:
        subparser = parser.add_parser(NAME, help=DESCRIPTION)
    subparser.set_defaults(name=NAME)
    subparser.add_argument(
        'localStreamName', type=str,
        help='the original stream name')
    subparser.add_argument(
        'aliasName', type=str,
        help='the alias alternative to the local stream name')
    subparser.add_argument(
        '--expire-period', type=int, dest='expirePeriod',
        help='the expiration period for this alias')


def main():
    # create the top-level parser
    parser = get_parser(DESCRIPTION)

    subparser(parser)

    args = parser.parse_args()
    api_wrapper(parser, **args.__dict__)


if __name__ == '__main__':
    main()
