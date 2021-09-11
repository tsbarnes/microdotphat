import logging

try:
    from local_settings import LOGLEVEL
except ImportError:
    LOGLEVEL = logging.DEBUG

try:
    from local_settings import MODULES
except ImportError:
    MODULES = [
        'apps.thermal',
        'apps.graph',
        'apps.scrolling_text',
    ]
