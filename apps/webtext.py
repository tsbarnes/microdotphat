import time
import logging
from microdotphat import write_string, scroll, show, clear
import posix_ipc


class App:
    mq: posix_ipc.MessageQueue = None

    def __init__(self):
        try:
            self.mq = posix_ipc.MessageQueue("/webtext_ipc", flags=posix_ipc.O_CREAT)
        except posix_ipc.PermissionsError:
            logging.error("Couldn't open webtext message queue")
        self.mq.block = False
        write_string(" Waiting... ")

    def run_once(self):
        scroll()
        show()
        try:
            message = self.mq.receive(timeout=10)
        except posix_ipc.BusyError:
            message = None

        if message:
            clear()
            write_string(" " + message[0].decode() + " ")


if __name__ == '__main__':
    app = App()

    while True:
        app.run_once()
        time.sleep(1)
