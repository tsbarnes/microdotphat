import time
import logging
from microdotphat import write_string, scroll, show, clear
import posix_ipc
import settings
from apps import AbstractApp


class App(AbstractApp):
    mq: posix_ipc.MessageQueue = None
    text: str = settings.WEBTEXT_DEFAULT

    def __init__(self):
        self.reload()

    def write(self, text=None):
        if text:
            self.text = text
        clear()
        write_string(self.text)

    def reload(self):
        self.write()
        if not self.mq:
            self.init_mq()

    def init_mq(self):
        try:
            self.mq = posix_ipc.MessageQueue("/webtext_ipc", flags=posix_ipc.O_CREAT)
            self.mq.block = False
        except posix_ipc.PermissionsError:
            logging.error("Couldn't open webtext message queue")

    def run_once(self):
        scroll()
        show()

        if not self.mq:
            self.init_mq()
        if self.mq:
            try:
                message = self.mq.receive(timeout=10)
            except posix_ipc.BusyError:
                message = None

            if message:
                self.write(" " + message[0].decode() + " ")


if __name__ == '__main__':
    app = App()

    while True:
        app.run_once()
        time.sleep(1)
