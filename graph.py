#!/usr/bin/env python

import os
from time import sleep
from random import randint

from microdotphat import set_col, show, clear


print("""Graph

Plots load average across the screen in a bar graph.

Press Ctrl+C to exit.
""")

graph = []
filled = True

while True:
    clear()
    #print(int(round(os.getloadavg()[0] * 2)))
    graph += [int(round(os.getloadavg()[0] * 2))]
    while len(graph) > 45:
        graph.pop(0)

    for x, val in enumerate(graph):
        if filled:
            set_col(x + (45-len(graph)), [
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
    sleep(5.00)