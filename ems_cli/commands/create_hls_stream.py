from . import BaseCommand


class Command(BaseCommand):
    name = 'create_hls_stream'

    description = 'create an HTTP Live Stream (HLS) out of an existing ' \
                  'H.264/AAC stream'

    quiet_fields = {
        'localStreamNames': 'local stream names'
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'localStreamNames', type=str,
            help='the stream(s) that will be used as the input')
        self.parser.add_argument(
            'targetFolder', type=str,
            help='the folder where all the .ts/.m3u8 files will be stored')
        self.parser.add_argument(
            '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
            help='if (1) the EMS will attempt to reconnect to the stream '
                 'source if the connection is severed')
        self.parser.add_argument(
            '--overwrite-destination', type=int, choices=[0, 1],
            dest='overwriteDestination',
            help='if (1), it will force overwrite of destination files')
        self.parser.add_argument(
            '--stale-retention-count', type=int, dest='staleRetentionCount',
            help='the number of old files kept besides the ones listed in the '
                 'current version of the playlist')
        self.parser.add_argument(
            '--create-master-playlist', type=int, choices=[0, 1],
            dest='createMasterPlaylist',
            help='if (1), a master playlist will be created')
        self.parser.add_argument(
            '--cleanup-destination', type=int, choices=[0, 1],
            dest='cleanupDestination',
            help='if (1), all *.ts and *.m3u8 files in the target folder '
                 'will be removed before HLS creation is started')
        self.parser.add_argument(
            '--bandwidths', type=str,
            help='the corresponding bandwidths for each stream listed in '
                 'localStreamNames')
        self.parser.add_argument(
            '--group-name', type=str, dest='groupName',
            help='the name assigned to the HLS stream or group')
        self.parser.add_argument(
            '--playlist-type', type=str, choices=['appending', 'rolling'],
            dest='playlistType', help='playlist type')
        self.parser.add_argument(
            '--playlist-length', type=int, dest='playlistLength',
            help='the length (number of elements) of the playlist')
        self.parser.add_argument(
            '--playlist-name', type=str, dest='playlistName',
            help='the file name of the playlist (*.m3u8)')
        self.parser.add_argument(
            '--chunk-length', type=int, dest='chunkLength',
            help='the length (in seconds) of each playlist element (*.ts file)')
        self.parser.add_argument(
            '--max-chunk-length', type=int, dest='maxChunkLength',
            help='maximum length (in seconds) the EMS will allow any single '
                 'chunk to be')
        self.parser.add_argument(
            '--chunk-base-name', type=str, dest='chunkBaseName',
            help='the base name used to generate the *.ts chunks')
        self.parser.add_argument(
            '--chunk-on-idr', type=int, choices=[0, 1], dest='chunkOnIDR',
            help='if (1) chunking is performed only on IDR, otherwise  '
                 'whenever chunk length is achieved')
        self.parser.add_argument(
            '--drm-type', type=str,
            choices=['none', 'evo', 'SAMPLE-AES', 'verimatrix'],
            dest='drmType', help='type of DRM encryption to use')
        self.parser.add_argument(
            '--aes-key-count', type=int, dest='AESKeyCount',
            help='number of keys that will be automatically generated and '
                 'rotated over while encrypting this HLS stream')
        self.parser.add_argument(
            '--audio-only', type=int, choices=[0, 1],
            dest='audioOnly', help='if (1), stream will be audio only')
        self.parser.add_argument(
            '--hls-resume', type=int, choices=[0, 1], dest='hlsResume',
            help='if (1), HLS will resume in appending segments to previously '
                 'created child playlist')
        self.parser.add_argument(
            '--cleanup-on-close', type=int, choices=[0, 1],
            dest='cleanupOnClose',
            help='if (1), corresponding hls files to a stream will be deleted '
                 'if the said stream is removed or shut down or disconnected')
        self.parser.add_argument(
            '--use-byte-range', type=int, choices=[0, 1], dest='useByteRange',
            help='if (1), will use the EXT-X-BYTERANGE feature of HLS (version '
                 '4 and up)')
        self.parser.add_argument(
            '--file-length', type=int, dest='fileLength',
            help='size of file before chunking it to another file (when '
                 '--use-byte-range=1)')
        self.parser.add_argument(
            '--use-system-time', type=int, choices=[0, 1], dest='useSystemTime',
            help='if (1), uses UTC in playlist time stamp otherwise will use '
                 'the local server time')
        self.parser.add_argument(
            '--offset-time', type=int, dest='offsetTime', help='?')
        self.parser.add_argument(
            '--start-offset', type=int, dest='startOffset',
            help='start offset time (in seconds) for the playback of the '
                 'playlist (HLS >= v.6)')


def main():
    Command().run()
