from .utils import BaseCommand


class Command(BaseCommand):
    name = 'push_stream'

    description = 'push a local stream to an external destination'

    quiet_fields = {
        'configId': 'config id',
        'localStreamName': 'stream name',
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'uri', type=int, help='the URI of the external stream')
        self.parser.add_argument(
            '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
            help='if (1) the EMS will attempt to reestablish connection with '
                 'a stream source after a connection has been lost')
        self.parser.add_argument(
            '--local-stream-name', type=str, dest='localStreamName',
            help='the stream name')
        self.parser.add_argument(
            '--target-stream-name', type=str, dest='targetStreamName',
            help='the name of the stream at destination')
        self.parser.add_argument(
            '--target-stream-type', type=str,
            choices=['live', 'record', 'append'], dest='targetStreamType',
            help='stream type (only for RTMP)')
        self.parser.add_argument(
            '--tc-url', type=str, dest='tcUrl', help='TC URL')
        self.parser.add_argument(
            '--page-url', type=str, dest='pageUrl',
            help='originating web page address')
        self.parser.add_argument(
            '--swf-url', type=str, dest='swfUrl', help='originating swf URL')
        self.parser.add_argument(
            '--ttl', type=int, help='socket IP_TTL option (time to live)')
        self.parser.add_argument(
            '--tos', type=int, help='socket IP_TOP option (type of service)')
        self.parser.add_argument(
            '--emulate-user-agent', type=str, dest='emulateUserAgent',
            help='user agent string (only RTMP)')
        self.parser.add_argument(
            '--rtmp-absolute-timestamps', type=int, choices=[0, 1],
            dest='rtmpAbsoluteTimestamps',
            help='if (1) forces the timestamps to be absolute (only RTMP)')
        self.parser.add_argument(
            '--send-chunk-size-request', type=int, choices=[0, 1],
            dest='sendChunkSizeRequest',
            help='if (1) send a "Set Chunk Length" message (only RTMP)')
        self.parser.add_argument(
            '--use-source-pts', type=int, choices=[0, 1], dest='useSourcePts',
            help='if (1) timestamps on source inbound RTMP stream are passed '
                 'directly to the outbound (pushed) RTMP streams')


def main():
    Command().run()
