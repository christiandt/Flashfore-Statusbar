#!/usr/bin/python

from progressreader import ProgressReader
import time
import sys
import os

env_printer_ip = os.getenv("FLASHFORGE_IP", "10.0.0.111")
env_printer_port = os.getenv("FLASHFORGE_PORT", 8899)
progress_reader = ProgressReader(env_printer_ip, env_printer_port)

try:
    SLEEP_TIME = float(sys.argv[1])
except:
    SLEEP_TIME = 10

while True:
    progress_reader.update_progress()
    progress_reader.print_progress()

    time.sleep(SLEEP_TIME)
