import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('records any inbound stream')

    quiet_fields = {
        'configId': _('config id'),
        'localStreamName': _('stream name'),
    }

    def fill_arguments(self):
        self.parser.add_argument(
            'localStreamName', type=str,
            help=_('the name of the stream to be used as input for recording'))
        self.parser.add_argument(
            'pathToFile', type=str, help=_('path and file name to write to'))
        self.parser.add_argument(
            '--type', type=str, choices=['ts', 'mp4', 'flv'],
            help=_('file type'))
        self.parser.add_argument(
            '--overwrite', type=int, choices=[0, 1],
            help=_('if (1) overwrite file, otherwise create a new file'))
        self.parser.add_argument(
            '--keep-alive', type=int, choices=[0, 1], dest='keepAlive',
            help=_('if (1) the EMS will attempt to reestablish connection '
                   'with a stream source after a connection has been lost'))
        self.parser.add_argument(
            '--chunk-length', type=int, dest='chunkLength',
            help=_('start a new recording file after ChunkLength seconds have '
                   'elapsed'))
        self.parser.add_argument(
            '--wait-for-idr', type=int, choices=[0, 1], dest='waitForIDR',
            help=_('if (1) new files will only be created on IDR boundaries'))
        self.parser.add_argument(
            '--win-qt-compat', type=int, choices=[0, 1], dest='winQtCompat',
            help=_('if (1) mandates 32bit header fields to ensure '
                   'compatibility with Windows QuickTime'))
        self.parser.add_argument(
            '--date-folder-structure', type=int, choices=[0, 1],
            dest='dateFolderStructure',
            help=_('if (1) folders will be created with names in YYYYMMDD '
                   'format'))


def main():
    Command().run()
