import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('pull in a stream from an external source')

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
            '--force-tcp', type=int, choices=[0, 1], dest='forceTcp',
            help=_('if (1) a TCP connection will be forced (only RTSP)'))
        self.parser.add_argument(
            '--tc-url', type=str, dest='tcUrl', help=_('TC URL'))
        self.parser.add_argument(
            '--page-url', type=str, dest='pageUrl',
            help=_('originating web page address'))
        self.parser.add_argument(
            '--swf-url', type=str, dest='swfUrl',
            help=_('originating swf URL'))
        self.parser.add_argument(
            '--range-start', type=int, dest='rangeStart',
            help=_('from which the playback should start (in seconds)'))
        self.parser.add_argument(
            '--range-end', type=int, dest='rangeEnd',
            help=_('the length in seconds for the playback'))
        self.parser.add_argument(
            '--ttl', type=int, help=_('socket IP_TTL option (time to live)'))
        self.parser.add_argument(
            '--tos', type=int,
            help=_('socket IP_TOP option (type of service)'))
        self.parser.add_argument(
            '--rtcp-detection-interval', type=int,
            dest='rtcpDetectionInterval',
            help=_('how much time (in seconds) should the server wait for '
                   'RTCP packets before declaring the RTSP stream as a '
                   'RTCP-less stream'))
        self.parser.add_argument(
            '--emulate-user-agent', type=str, dest='emulateUserAgent',
            help=_('user agent string (only RTMP)'))
        self.parser.add_argument(
            '--is-audio', type=int, choices=[0, 1], dest='isAudio',
            help=_('if (1) it indicates that the currently pulled stream '
                   'is an audio source (only RTP)'))
        self.parser.add_argument(
            '--audio-codec-bytes', type=str, dest='audioCodecBytes',
            help=_('?'))
        self.parser.add_argument(
            '--sps-bytes', type=str, dest='spsBytes',
            help=_('the video SPS bytes of this RTP stream (base 64 encoded)'))
        self.parser.add_argument(
            '--pps-bytes', type=str, dest='ppsBytes',
            help=_('the video PPS bytes of this RTP stream (base 64 encoded)'))
        self.parser.add_argument(
            '--ssm-ip', type=str, dest='ssmIp',
            help=_('the source IP from source-specific-multicast'))
        self.parser.add_argument(
            '--http-proxy', type=str, dest='httpProxy',
            help=_('RTSP HTTP Proxy from which the RTSP stream should be '
                   'pulled (ip:port) or "self" for pulling RTSP over HTTP'))


def main():
    Command().run()
