#!/usr/bin/env python
import psutil
import time
import logging
from microdotphat import set_col, show, clear
from apps import AbstractApp


class App(AbstractApp):
    graph = []
    filled = True

    def run_once(self):
        clear()

        load_average = psutil.getloadavg()[0]
        pixels = int(load_average * 3)
        if pixels > 7:
            logging.warning("Load Average: {0} results in {1} pixels, max is 7".format(load_average, pixels))
            pixels = 7

        self.graph += [pixels]
        while len(self.graph) > 45:
            self.graph.pop(0)

        for index, value in enumerate(self.graph):
            if self.filled:
                set_col(index + (45 - len(self.graph)), [
                    0,
                    0b1000000,
                    0b1100000,
                    0b1110000,
                    0b1111000,
                    0b1111100,
                    0b1111110,
                    0b1111111][value])
            else:
                set_col(index, 1 << (7 - value))

        show()


if __name__ == '__main__':
    app = App()

    while True:
        app.run_once()
        time.sleep(1)
