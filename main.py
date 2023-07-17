#!/usr/bin/python

from progressreader import ProgressReader
from preferences import Preferences
import time
import sys
import os

prefs = Preferences()
port = int(os.getenv('FLASHFOREGE_PORT', prefs.port))
progress_reader = ProgressReader(prefs.ip, port)

try:
    SLEEP_TIME = float(sys.argv[1])
except:
    SLEEP_TIME = 10

while True:
    progress_reader.update_progress()
    progress_reader.print_progress()

    time.sleep(SLEEP_TIME)
