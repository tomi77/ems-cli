import argparse

from ems_cli.utils import api_wrapper, get_parser


DESCRIPTION = 'create Dynamic Adaptive Streaming over HTTP (DASH) out of ' \
              'an existing H.264/AAC stream'
NAME = 'create_dash_stream'


def subparser(parser):
    """create the parser for the "create_dash_stream" command"""
    if not isinstance(parser, argparse._SubParsersAction):
        subparser = parser
    else:
        subparser = parser.add_parser(NAME, help=DESCRIPTION)
    subparser.set_defaults(name=NAME)
    subparser.add_argument(
        'localStreamNames', type=str,
        help='the stream(s) that will be used as the input')
    subparser.add_argument(
        'targetFolder', type=str,
        help='the folder where all the manifest and fragment files will be '
             'stored')
    subparser.add_argument(
        '--bandwidths', type=str,
        help='the corresponding bandwidths for each stream listed in '
             'localStreamNames')
    subparser.add_argument(
        '--group-name', type=str, dest='groupName',
        help='the name assigned to the DASH stream or group')
    subparser.add_argument(
        '--playlist-type', type=str, choices=['appending', 'rolling'],
        dest='playlistType', help='playlist type')
    subparser.add_argument(
        '--playlist-length', type=int, dest='playlistLength',
        help='the number of fragments before the server starts to overwrite '
             'the older fragments')
    subparser.add_argument(
        '--manifest-name', type=str, dest='manifestName',
        help='the manifest file name')
    subparser.add_argument(
        '--chunk-length', type=int, dest='chunkLength',
        help='the length (in seconds) of fragments to be made')
    subparser.add_argument(
        '--chunk-on-idr', type=int, choices=[0, 1], dest='chunkOnIDR',
        help='if (1) chunking is performed only on IDR, otherwise  whenever '
             'chunk length is achieved')
    subparser.add_argument(
        '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
        help='if (1) the EMS will attempt to reconnect to the stream source '
             'if the connection is severed')
    subparser.add_argument(
        '--overwrite-destination', type=int, choices=[0, 1],
        dest='overwriteDestination',
        help='if (1), it will allow overwrite of destination files')


def main():
    # create the top-level parser
    parser = get_parser(DESCRIPTION)

    subparser(parser)

    args = parser.parse_args()
    api_wrapper(parser, **args.__dict__)


if __name__ == '__main__':
    main()
