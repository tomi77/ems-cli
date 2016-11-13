import os

from . import BaseCommand


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = 'pull in a stream from an external source'

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
            '--force-tcp', type=int, choices=[0, 1], dest='forceTcp',
            help='if (1) a TCP connection will be forced (only RTSP)')
        self.parser.add_argument(
            '--tc-url', type=str, dest='tcUrl', help='TC URL')
        self.parser.add_argument(
            '--page-url', type=str, dest='pageUrl',
            help='originating web page address')
        self.parser.add_argument(
            '--swf-url', type=str, dest='swfUrl', help='originating swf URL')
        self.parser.add_argument(
            '--range-start', type=int, dest='rangeStart',
            help='from which the playback should start (in seconds)')
        self.parser.add_argument(
            '--range-end', type=int, dest='rangeEnd',
            help='the length in seconds for the playback')
        self.parser.add_argument(
            '--ttl', type=int, help='socket IP_TTL option (time to live)')
        self.parser.add_argument(
            '--tos', type=int, help='socket IP_TOP option (type of service)')
        self.parser.add_argument(
            '--rtcp-detection-interval', type=int,
            dest='rtcpDetectionInterval',
            help='how much time (in seconds) should the server wait for RTCP '
                 'packets before declaring the RTSP stream as a RTCP-less '
                 'stream')
        self.parser.add_argument(
            '--emulate-user-agent', type=str, dest='emulateUserAgent',
            help='user agent string (only RTMP)')
        self.parser.add_argument(
            '--is-audio', type=int, choices=[0, 1], dest='isAudio',
            help='if (1) it indicates that the currently pulled stream '
                 'is an audio source (only RTP)')
        self.parser.add_argument(
            '--audio-codec-bytes', type=str, dest='audioCodecBytes',
            help='')
        self.parser.add_argument(
            '--sps-bytes', type=str, dest='spsBytes',
            help='the video SPS bytes of this RTP stream (base 64 encoded)')
        self.parser.add_argument(
            '--pps-bytes', type=str, dest='ppsBytes',
            help='the video PPS bytes of this RTP stream (base 64 encoded)')
        self.parser.add_argument(
            '--ssm-ip', type=str, dest='ssmIp',
            help='the source IP from source-specific-multicast')
        self.parser.add_argument(
            '--http-proxy', type=str, dest='httpProxy',
            help='RTSP HTTP Proxy from which the RTSP stream should be '
                 'pulled (ip:port) or "self" for pulling RTSP over HTTP')


def main():
    Command().run()
