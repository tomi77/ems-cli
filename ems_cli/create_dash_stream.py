from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'create_dash_stream'

    description = 'create Dynamic Adaptive Streaming over HTTP (DASH) out ' \
                  'of an existing H.264/AAC stream'

    def _fill_arguments(self, parser):
        parser.add_argument(
            'localStreamNames', type=str,
            help='the stream(s) that will be used as the input')
        parser.add_argument(
            'targetFolder', type=str,
            help='the folder where all the manifest and fragment files will be '
                 'stored')
        parser.add_argument(
            '--bandwidths', type=str,
            help='the corresponding bandwidths for each stream listed in '
                 'localStreamNames')
        parser.add_argument(
            '--group-name', type=str, dest='groupName',
            help='the name assigned to the DASH stream or group')
        parser.add_argument(
            '--playlist-type', type=str, choices=['appending', 'rolling'],
            dest='playlistType', help='playlist type')
        parser.add_argument(
            '--playlist-length', type=int, dest='playlistLength',
            help='the number of fragments before the server starts to '
                 'overwrite the older fragments')
        parser.add_argument(
            '--manifest-name', type=str, dest='manifestName',
            help='the manifest file name')
        parser.add_argument(
            '--chunk-length', type=int, dest='chunkLength',
            help='the length (in seconds) of fragments to be made')
        parser.add_argument(
            '--chunk-on-idr', type=int, choices=[0, 1], dest='chunkOnIDR',
            help='if (1) chunking is performed only on IDR, otherwise whenever '
                 'chunk length is achieved')
        parser.add_argument(
            '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
            help='if (1) the EMS will attempt to reconnect to the stream '
                 'source if the connection is severed')
        parser.add_argument(
            '--overwrite-destination', type=int, choices=[0, 1],
            dest='overwriteDestination',
            help='if (1), it will allow overwrite of destination files')


def main():
    Command().run()