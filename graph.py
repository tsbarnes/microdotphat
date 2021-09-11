#!/usr/bin/env python
import psutil
import time
from microdotphat import set_col, show, clear


class App:
    graph = []
    filled = True

    def run_once(self):
        clear()

        cpu_percent = psutil.cpu_percent()
        pixels = int(cpu_percent / 12.5) - 1

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
