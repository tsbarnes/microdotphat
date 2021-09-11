#!/usr/bin/env python3
import logging
import time
import posix_ipc
import importlib
import settings


class App:
    modules = []
    current_module = None

    def __init__(self):
        for module_name in settings.MODULES:
            lib = importlib.import_module(module_name)
            self.modules.append(lib.App())
        self.current_module = self.modules[0]

        self.mq = posix_ipc.MessageQueue("/microdotphat_ipc", flags=posix_ipc.O_CREAT)
        self.mq.block = False

        for module in self.modules:
            module.run_once()

        try:
            message = self.mq.receive(timeout=10)
        except posix_ipc.BusyError:
            message = None

        if message:
            logging.debug("Received message: " + message)

    def run(self):
        time.sleep(1)


app = App()
while True:
    app.run()
