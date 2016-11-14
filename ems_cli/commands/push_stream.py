import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('push a local stream to an external destination')

    quiet_fields = {
        'configId': _('config id'),
        'localStreamName': _('stream name'),
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'uri', type=int, help=_('the URI of the external stream'))
        self.parser.add_argument(
            '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
            help=_('if (1) the EMS will attempt to reestablish connection '
                   'with a stream source after a connection has been lost'))
        self.parser.add_argument(
            '--local-stream-name', type=str, dest='localStreamName',
            help=_('the stream name'))
        self.parser.add_argument(
            '--target-stream-name', type=str, dest='targetStreamName',
            help=_('the name of the stream at destination'))
        self.parser.add_argument(
            '--target-stream-type', type=str,
            choices=['live', 'record', 'append'], dest='targetStreamType',
            help=_('stream type (only for RTMP)'))
        self.parser.add_argument(
            '--tc-url', type=str, dest='tcUrl', help=_('TC URL'))
        self.parser.add_argument(
            '--page-url', type=str, dest='pageUrl',
            help=_('originating web page address'))
        self.parser.add_argument(
            '--swf-url', type=str, dest='swfUrl',
            help=_('originating swf URL'))
        self.parser.add_argument(
            '--ttl', type=int, help=_('socket IP_TTL option (time to live)'))
        self.parser.add_argument(
            '--tos', type=int,
            help=_('socket IP_TOP option (type of service)'))
        self.parser.add_argument(
            '--emulate-user-agent', type=str, dest='emulateUserAgent',
            help=_('user agent string (only RTMP)'))
        self.parser.add_argument(
            '--rtmp-absolute-timestamps', type=int, choices=[0, 1],
            dest='rtmpAbsoluteTimestamps',
            help=_('if (1) forces the timestamps to be absolute (only RTMP)'))
        self.parser.add_argument(
            '--send-chunk-size-request', type=int, choices=[0, 1],
            dest='sendChunkSizeRequest',
            help=_('if (1) send a "Set Chunk Length" message (only RTMP)'))
        self.parser.add_argument(
            '--use-source-pts', type=int, choices=[0, 1], dest='useSourcePts',
            help=_('if (1) timestamps on source inbound RTMP stream are '
                   'passed directly to the outbound (pushed) RTMP streams'))


def main():
    Command().run()
