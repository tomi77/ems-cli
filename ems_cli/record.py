from ems_cli.utils import BaseCommand


class Command(BaseCommand):
    name = 'record'

    description = 'records any inbound stream'

    quiet_fields = {
        'configId': 'config id',
        'localStreamName': 'stream name',
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'localStreamName', type=str,
            help='the name of the stream to be used as input for recording')
        self.parser.add_argument(
            'pathToFile', type=str, help='path and file name to write to')
        self.parser.add_argument(
            '--type', type=str, choices=['ts', 'mp4', 'flv'], help='file type')
        self.parser.add_argument(
            '--overwrite', type=int, choices=[0, 1],
            help='if (1) overwrite file, otherwise create a new file')
        self.parser.add_argument(
            '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
            help='if (1) the EMS will attempt to reestablish connection with '
                 'a stream source after a connection has been lost')
        self.parser.add_argument(
            '--chunk-length', type=int, dest='chunkLength',
            help='start a new recording file after ChunkLength seconds have '
                 'elapsed')
        self.parser.add_argument(
            '--wait-for-idr', type=int, choices=[0, 1], dest='waitForIDR',
            help='if (1) new files will only be created on IDR boundaries')
        self.parser.add_argument(
            '--win-qt-compat', type=int, choices=[0, 1], dest='winQtCompat',
            help='if (1) mandates 32bit header fields to ensure '
                 'compatibility with Windows QuickTime')
        self.parser.add_argument(
            '--date-folder-structure', type=int, choices=[0, 1],
            dest='dateFolderStructure',
            help='if (1) folders will be created with names in YYYYMMDD '
                 'format')


def main():
    Command().run()
