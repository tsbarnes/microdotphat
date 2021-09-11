#!/usr/bin/env python
import logging
import time
import microdotphat


class App:
    path = "/sys/class/thermal/thermal_zone0/temp"
    file = None
    temp_raw = None
    temp = None

    def run_once(self):
        microdotphat.clear()
        self.file = open(self.path, "r")
        self.temp_raw = int(self.file.read().strip())
        logging.debug(self.temp_raw)
        self.temp = float(self.temp_raw / 1000.0)
        microdotphat.write_string("%.2f" % self.temp + "c", kerning=False)
        logging.debug("Displaying temperature: %.2f" % self.temp + "c")
        microdotphat.show()


if __name__ == '__main__':
    app = App()

    while True:
        app.run_once()
        time.sleep(1)
