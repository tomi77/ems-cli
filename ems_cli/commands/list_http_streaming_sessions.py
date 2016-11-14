import os

from . import BaseCommand
from ..i18n import _


class Command(BaseCommand):
    name = os.path.splitext(os.path.basename(__file__))[0]

    description = _('all currently active HTTP streaming sessions')

    quiet_fields = {
        'clientIP': _('client ip'),
        'sessionId': _('session id'),
    }

    def fill_arguments(self):
        pass


def main():
    Command().run()
