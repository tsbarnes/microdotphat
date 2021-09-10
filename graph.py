#!/usr/bin/env python
from time import sleep

from gpiozero import LoadAverage
from microdotphat import set_col, show, clear


print("""Graph

Plots load average across the screen in a bar graph.

Press Ctrl+C to exit.
""")


class Graph:
    graph = []
    filled = True

    def iterate_loop(self):
        clear()
        print(LoadAverage(minutes=1).load_average)
        self.graph += [int(LoadAverage(minutes=1).load_average)]
        while len(self.graph) > 45:
            self.graph.pop(0)

        for x, val in enumerate(self.graph):
            if self.filled:
                set_col(x + (45-len(self.graph)), [
                    0,
                    0b1000000,
                    0b1100000,
                    0b1110000,
                    0b1111000,
                    0b1111100,
                    0b1111110,
                    0b1111111][val])
            else:
                set_col(x, 1 << (7-val))

        show()

    def main_loop(self):
        while True:
            self.iterate_loop()
            sleep(1)


if __name__ == '__main__':
    graph = Graph()
    graph.main_loop()
