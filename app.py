import psutil
import time
import sys
import importlib
import microdotphat
import settings


class App:
    modules = []
    current_module = None

    def __init__(self):
        for module_name in settings.MODULES:
            self.modules.append(importlib.import_module(module_name))
        self.current_module = self.modules[0]


app = App()
