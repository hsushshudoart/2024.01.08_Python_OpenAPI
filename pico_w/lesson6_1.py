#machine.freq()  # get the current frequency of the CPU

import machine
import time

while True:
    print(machine.freq(),"MHz")
    time.sleep(1)