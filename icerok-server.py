#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-
from serial import Serial
import time
from pathlib import Path

from serial.serialutil import SerialException

SERIAL = "/dev/ttyUSB1"
TIMEOUT = 100
FILENAME = "data.raw"
BYTES = 1


# ------------------ Main
if __name__ == "__main__":

    # -- Open the serial port
    try:
      serial_p = Serial(SERIAL, 12000000)
      time.sleep(0.2)
    except SerialException as e:
        print("Error al abrir puerto serie ")
        code, msg = e.args
        print(msg)
        exit()

    print("\nWaiting for the Data from the FPGA...")
    count=0;
    while True:
        try:
            data = serial_p.read(BYTES)
        except KeyboardInterrupt:
            print("\nABORT...")
            break

        print(f'{hex(data[0])} ', end='', flush=True)
        count = count + 1;

        if (count % 16 == 0):
          print("")

        # Write the data into the file
        # p = Path('.')
        # f_data = p / FILENAME
        # f_data.write_bytes(data)

        # print(f"FILE: {f_data.name}\n")

    serial_p.close()