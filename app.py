#!/usr/bin/env python3
import logging
import time
import posix_ipc
import importlib
import settings


class App:
    modules = []

    apps = []
    current_app = None
    current_app_index = 0

    def __init__(self):
        logging.basicConfig(level=settings.LOGLEVEL)

        for module_name in settings.MODULES:
            self.modules.append(importlib.import_module(module_name))

        self.mq = posix_ipc.MessageQueue("/microdotphat_ipc", flags=posix_ipc.O_CREAT)
        self.mq.block = False

        for module in self.modules:
            self.apps.append(module.App())
        self.current_app = self.apps[self.current_app_index]

    def change_app(self, index):
        self.current_app = self.apps[index]
        self.current_app_index = index

    def run(self):
        self.current_app.run_once()

        try:
            message = self.mq.receive(timeout=10)
        except posix_ipc.BusyError:
            message = None

        if message:
            message_text = message[0].decode()
            logging.debug("Received message: " + message_text)

            if message_text == "next":
                next_app_index = (self.current_app_index + 1) % len(self.apps)
                logging.debug("Current app index: {0}, next app index: {1}".format(
                    self.current_app_index,
                    next_app_index
                ))
                self.change_app(next_app_index)
            elif message_text == "previous":
                previous_app_index = (self.current_app_index + len(self.apps) - 1) % len(self.apps)
                logging.debug("Current app index: {0}, previous app index: {1}".format(
                    self.current_app_index,
                    previous_app_index
                ))
                self.change_app(previous_app_index)


if __name__ == '__main__':
    app = App()

    while True:
        app.run()
        time.sleep(1)
