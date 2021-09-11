#!/usr/bin/env python3
import logging
import sys
import time
import microdotphat


class App:
    text = "Waiting...      "

    def write(self, text=None):
        if text:
            self.text = text
        microdotphat.write_string(self.text, offset_x=0)

    def run_once(self):
        microdotphat.clear()
        microdotphat.write_string(self.text, offset_x=0)
        microdotphat.scroll()
        microdotphat.show()


if __name__ == '__main__':
    app = App()

    if len(sys.argv) > 1:
        app.text = " ".join(sys.argv[1:])

    while True:
        app.write()
        app.run_once()
        time.sleep(1)
