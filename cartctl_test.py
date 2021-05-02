#!/usr/bin/env python3
"""
Example of usage/test of Cart controller implementation.
"""

from cartctl import CartCtl, reset_scheduler
from cart import Cart, Load
import jarvisenv
import csv

def add_load(c: CartCtl, load: Load):
    "callback for schedulled load"
    print('%d requesting %s %s %s %d' % \
        (jarvisenv.time(), load.src, load.dst, load.content, load.weight))
    c.request(load)

def main(filename):
    "main test suite"
    # Setup
    # 4 slots, 150 kg max load capacity, 2=max debug
    cart_dev = Cart(4, 150, 1)
    #cart_dev.onmove = on_move

    c = CartCtl(cart_dev, jarvisenv.JARVIS_TRACKS)

    s = reset_scheduler()

    with open(filename) as reqfile:
        reqreader = csv.reader(reqfile)
        for request in reqreader:
            load = Load(request[1], request[2], int(request[3]), request[4])
            s.enter(int(request[0]), 0, add_load, (c,load))

    # Exercise & Verify
    s.run()

    print('%d stop' % jarvisenv.time())
#    print(cart_dev)

if __name__ == "__main__":
    filename = 'requests.csv'
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    main(filename)
