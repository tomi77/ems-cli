import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('create a Microsoft Smooth Stream (MSS) out of an '
                    'existing H.264/AAC stream')

    quiet_fields = {
        'localStreamNames': _('local stream names')
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'localStreamNames', type=str,
            help=_('the stream(s) that will be used as the input'))
        self.parser.add_argument(
            'targetFolder', type=str,
            help=_('the folder where all the manifest and fragment files '
                   'will be stored'))
        self.parser.add_argument(
            '--bandwidths', type=str,
            help=_('the corresponding bandwidths for each stream listed in '
                   'localStreamNames'))
        self.parser.add_argument(
            '--group-name', type=str, dest='groupName',
            help=_('the name assigned to the MSS stream or group'))
        self.parser.add_argument(
            '--playlist-type', type=str, choices=['appending', 'rolling'],
            dest='playlistType', help=_('playlist type'))
        self.parser.add_argument(
            '--playlist-length', type=int, dest='playlistLength',
            help=_('the number of fragments before the server starts to '
                   'overwrite the older fragments'))
        self.parser.add_argument(
            '--manifest-name', type=str, dest='manifestName',
            help=_('the manifest file name'))
        self.parser.add_argument(
            '--chunk-length', type=int, dest='chunkLength',
            help=_('the length (in seconds) of fragments to be made'))
        self.parser.add_argument(
            '--chunk-on-idr', type=int, choices=[0, 1], dest='chunkOnIDR',
            help=_('if (1) chunking is performed only on IDR, otherwise  '
                   'whenever chunk length is achieved'))
        self.parser.add_argument(
            '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
            help=_('if (1) the EMS will attempt to reconnect to the stream '
                   'source if the connection is severed'))
        self.parser.add_argument(
            '--overwrite-destination', type=int, choices=[0, 1],
            dest='overwriteDestination',
            help=_('if (1), it will allow overwrite of destination files'))
        self.parser.add_argument(
            '--stale-retention-count', type=int, dest='staleRetentionCount',
            help=_('the number of old files kept besides the ones listed in '
                   'the current version of the playlist'))
        self.parser.add_argument(
            '--cleanup-destination', type=int, choices=[0, 1],
            dest='cleanupDestination',
            help=_('if (1), all manifest and fragment files in the target '
                   'folder will be removed before MSS creation is started'))
        self.parser.add_argument(
            '--ism-type', type=int, choices=[0, 1], dest='ismType',
            help=_('either ismc for serving content to client or isml for '
                   'serving content to smooth server'))
        self.parser.add_argument(
            '--is-live', type=int, choices=[0, 1], dest='isLive',
            help=_('if (1), creates a live MSS stream, otherwise for VOD'))
        self.parser.add_argument(
            '--publishing-point', type=str, dest='publishingPoint',
            help=_('the REST URI where the mss contents will be ingested '
                   '(ismType=isml)'))
        self.parser.add_argument(
            '--ingest-mode', type=str, dest='ingestMode',
            choices=['single', 'loop'],
            help=_('non looping or looping ingest'))


def main():
    Command().run()
