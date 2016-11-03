import argparse

from ems_cli.utils import api_wrapper, get_parser


DESCRIPTION = 'creates secondary name(s) for group name'
NAME = 'add_group_name_alias'


def subparser(parser):
    """create the parser for the "add_group_name_alias" command"""
    if not isinstance(parser, argparse._SubParsersAction):
        subparser = parser
    else:
        subparser = parser.add_parser(NAME, help=DESCRIPTION)
    subparser.set_defaults(name=NAME)
    subparser.add_argument(
        'groupName', type=str, help='the original group name')
    subparser.add_argument(
        'aliasName', type=str, help='the alias alternative to the group name')


def main():
    # create the top-level parser
    parser = get_parser(DESCRIPTION)

    subparser(parser)

    args = parser.parse_args()
    api_wrapper(parser, **args.__dict__)


if __name__ == '__main__':
    main()
