from . import BaseCommand


class Command(BaseCommand):
    name = 'transcode'

    description = 'change the compression characteristics of an ' \
                  'audio/video stream'

    quiet_fields = {
        'source': 'source'
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'source', type=str, help='uri or a local stream name')
        self.parser.add_argument(
            'destinations', type=str,
            help='the target URI(s) or stream name(s) of the transcoded '
                 'stream')
        self.parser.add_argument(
            '--target-stream-names', type=str, dest='targetStreamNames',
            help='the name of the stream(s) at destination(s)')
        self.parser.add_argument(
            '--group-name', type=str, dest='groupName', help='the group name')
        self.parser.add_argument(
            '--video-bitrates', type=str, dest='videoBitrates',
            help='target output video bitrate(s) (in bits/s, append k to '
                 'value for kbits/s)')
        self.parser.add_argument(
            '--video-sizes', type=str, dest='videoSizes',
            help='target output video size(s) in wxh (width x height) format')
        self.parser.add_argument(
            '--video-advanced-params-profiles', type=str,
            dest='videoAdvancedParamsProfiles',
            help='name of video profile template')
        self.parser.add_argument(
            '--audio-bitrates', type=str, dest='audioBitrates',
            help='target output audio bitrate(s) (in bits/s, append k to '
                 'value for kbits/s)')
        self.parser.add_argument(
            '--audio-channels-counts', type=str, dest='audioChannelsCounts',
            help='target output audio channel(s) count(s)')
        self.parser.add_argument(
            '--audio-frequencies', type=str, dest='audioFrequencies',
            help='target output audio frequency(ies) (in Hz, append k to '
                 'value for kHz)')
        self.parser.add_argument(
            '--audio-advanced-params-profiles', type=str,
            dest='audioAdvancedParamsProfiles',
            help='name of audio profile template')
        self.parser.add_argument(
            '--overlays', type=str, help='location of the overlay source(s)')
        self.parser.add_argument(
            '--croppings', type=str,
            help='target video cropping position(s) and size(s) in '
                 'left:top:width:height or width:height format')
        self.parser.add_argument(
            '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
            help='if (1), restart transcoding if it was previously activated')
        self.parser.add_argument(
            '--command-flags', type=str, dest='commandFlags',
            help='other commands to the transcode process')


def main():
    Command().run()
