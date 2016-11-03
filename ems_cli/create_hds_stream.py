import argparse

from ems_cli.utils import api_wrapper, get_parser


DESCRIPTION = 'create an HDS (HTTP Dynamic Streaming) stream out of an ' \
              'existing H.264/AAC stream'
NAME = 'create_hds_stream'


def subparser(parser):
    """create the parser for the "create_hds_stream" command"""
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
        help='the folder where all the manifest (*.f4m) and fragment (f4v*) '
             'files will be stored')
    subparser.add_argument(
        '--bandwidths', type=str,
        help='the corresponding bandwidths for each stream listed in '
             'localStreamNames')
    subparser.add_argument(
        '--chunk-base-name', type=str, dest='chunkBaseName',
        help='the base name used to generate the fragments')
    subparser.add_argument(
        '--chunk-length', type=int, dest='chunkLength',
        help='the length (in seconds) of fragments to be made')
    subparser.add_argument(
        '--chunk-on-idr', type=int, choices=[0, 1], dest='chunkOnIDR',
        help='if (1) chunking is performed only on IDR, otherwise  whenever '
             'chunk length is achieved')
    subparser.add_argument(
        '--group-name', type=str, dest='groupName',
        help='the name assigned to the HDS stream or group')
    subparser.add_argument(
        '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
        help='if (1) the EMS will attempt to reconnect to the stream source '
             'if the connection is severed')
    subparser.add_argument(
        '--manifest-name', type=str, dest='manifestName',
        help='the manifest file name')
    subparser.add_argument(
        '--overwrite-destination', type=int, choices=[0, 1],
        dest='overwriteDestination',
        help='if (1), it will allow overwrite of destination files')
    subparser.add_argument(
        '--playlist-type', type=str, choices=['appending', 'rolling'],
        dest='playlistType', help='playlist type')
    subparser.add_argument(
        '--playlist-length', type=int, dest='playlistLength',
        help='the number of fragments before the server starts to overwrite '
             'the older fragments')
    subparser.add_argument(
        '--stale-retention-count', type=int, dest='staleRetentionCount',
        help='the number of old files kept besides the ones listed in the '
             'current version of the playlist')
    subparser.add_argument(
        '--create-master-playlist', type=int, choices=[0, 1],
        dest='createMasterPlaylist',
        help='if (1), a master playlist will be created')
    subparser.add_argument(
        '--cleanup-destination', type=int, choices=[0, 1],
        dest='cleanupDestination',
        help='if (1), all manifest and fragment files in the target folder '
             'will be removed before HDS creation is started')


def main():
    # create the top-level parser
    parser = get_parser(DESCRIPTION)

    subparser(parser)

    args = parser.parse_args()
    api_wrapper(parser, **args.__dict__)


if __name__ == '__main__':
    main()
