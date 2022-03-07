#!/usr/bin/env python3

import time as time_module
from itertools import cycle
from time import sleep

for frame in cycle(r'-\|/'):
    print('\r', frame, sep='', end='', flush=True)
    sleep(0.2)
