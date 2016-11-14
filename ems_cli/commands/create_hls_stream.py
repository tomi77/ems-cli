import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('create an HTTP Live Stream (HLS) out of an existing '
                    'H.264/AAC stream')

    quiet_fields = {
        'localStreamNames': _('local stream names')
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'localStreamNames', type=str,
            help=_('the stream(s) that will be used as the input'))
        self.parser.add_argument(
            'targetFolder', type=str,
            help=_('the folder where all the .ts/.m3u8 files will be stored'))
        self.parser.add_argument(
            '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
            help=_('if (1) the EMS will attempt to reconnect to the stream '
                   'source if the connection is severed'))
        self.parser.add_argument(
            '--overwrite-destination', type=int, choices=[0, 1],
            dest='overwriteDestination',
            help=_('if (1), it will force overwrite of destination files'))
        self.parser.add_argument(
            '--stale-retention-count', type=int, dest='staleRetentionCount',
            help=_('the number of old files kept besides the ones listed in '
                   'the current version of the playlist'))
        self.parser.add_argument(
            '--create-master-playlist', type=int, choices=[0, 1],
            dest='createMasterPlaylist',
            help=_('if (1), a master playlist will be created'))
        self.parser.add_argument(
            '--cleanup-destination', type=int, choices=[0, 1],
            dest='cleanupDestination',
            help=_('if (1), all *.ts and *.m3u8 files in the target folder '
                   'will be removed before HLS creation is started'))
        self.parser.add_argument(
            '--bandwidths', type=str,
            help=_('the corresponding bandwidths for each stream listed in '
                   'localStreamNames'))
        self.parser.add_argument(
            '--group-name', type=str, dest='groupName',
            help=_('the name assigned to the HLS stream or group'))
        self.parser.add_argument(
            '--playlist-type', type=str, choices=['appending', 'rolling'],
            dest='playlistType', help=_('playlist type'))
        self.parser.add_argument(
            '--playlist-length', type=int, dest='playlistLength',
            help=_('the length (number of elements) of the playlist'))
        self.parser.add_argument(
            '--playlist-name', type=str, dest='playlistName',
            help=_('the file name of the playlist (*.m3u8)'))
        self.parser.add_argument(
            '--chunk-length', type=int, dest='chunkLength',
            help=_('the length (in seconds) of each playlist element '
                   '(*.ts file)'))
        self.parser.add_argument(
            '--max-chunk-length', type=int, dest='maxChunkLength',
            help=_('maximum length (in seconds) the EMS will allow any single '
                   'chunk to be'))
        self.parser.add_argument(
            '--chunk-base-name', type=str, dest='chunkBaseName',
            help=_('the base name used to generate the *.ts chunks'))
        self.parser.add_argument(
            '--chunk-on-idr', type=int, choices=[0, 1], dest='chunkOnIDR',
            help=_('if (1) chunking is performed only on IDR, otherwise  '
                   'whenever chunk length is achieved'))
        self.parser.add_argument(
            '--drm-type', type=str,
            choices=['none', 'evo', 'SAMPLE-AES', 'verimatrix'],
            dest='drmType', help=_('type of DRM encryption to use'))
        self.parser.add_argument(
            '--aes-key-count', type=int, dest='AESKeyCount',
            help=_('number of keys that will be automatically generated and '
                   'rotated over while encrypting this HLS stream'))
        self.parser.add_argument(
            '--audio-only', type=int, choices=[0, 1],
            dest='audioOnly', help=_('if (1), stream will be audio only'))
        self.parser.add_argument(
            '--hls-resume', type=int, choices=[0, 1], dest='hlsResume',
            help=_('if (1), HLS will resume in appending segments to '
                   'previously created child playlist'))
        self.parser.add_argument(
            '--cleanup-on-close', type=int, choices=[0, 1],
            dest='cleanupOnClose',
            help=_('if (1), corresponding hls files to a stream will be '
                   'deleted if the said stream is removed or shut down or '
                   'disconnected'))
        self.parser.add_argument(
            '--use-byte-range', type=int, choices=[0, 1], dest='useByteRange',
            help=_('if (1), will use the EXT-X-BYTERANGE feature of HLS '
                   '(version 4 and up)'))
        self.parser.add_argument(
            '--file-length', type=int, dest='fileLength',
            help=_('size of file before chunking it to another file (when '
                   '--use-byte-range=1)'))
        self.parser.add_argument(
            '--use-system-time', type=int, choices=[0, 1], dest='useSystemTime',
            help=_('if (1), uses UTC in playlist time stamp otherwise will '
                   'use the local server time'))
        self.parser.add_argument(
            '--offset-time', type=int, dest='offsetTime', help='?')
        self.parser.add_argument(
            '--start-offset', type=int, dest='startOffset',
            help=_('start offset time (in seconds) for the playback of the '
                   'playlist (HLS >= v.6)'))


def main():
    Command().run()
