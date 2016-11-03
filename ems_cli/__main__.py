import ems_cli
from ems_cli.utils import api_wrapper, get_parser


def main():
    # create the top-level parser
    parser = get_parser('EMS cli')
    subparsers = parser.add_subparsers(help='command')

    ems_cli.add_group_name_alias.subparser(subparsers)
    ems_cli.add_stream_alias.subparser(subparsers)
    ems_cli.create_dash_stream.subparser(subparsers)
    ems_cli.create_hds_stream.subparser(subparsers)
    ems_cli.create_hls_stream.subparser(subparsers)

    args = parser.parse_args()
    api_wrapper(parser, **args.__dict__)
