import logging
from apps import get_apps

try:
    from local_settings import LOGLEVEL
except ImportError:
    LOGLEVEL = logging.DEBUG

try:
    from local_settings import MODULES
except ImportError:
    MODULES = get_apps()

try:
    from local_settings import SCROLLING_TEXT_DEFAULT
except ImportError:
    SCROLLING_TEXT_DEFAULT = " Waiting "

try:
    from local_settings import WEBTEXT_DEFAULT
except ImportError:
    WEBTEXT_DEFAULT = " Waiting "
