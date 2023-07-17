# -*- coding: utf-8 -*-

import socket
import sys
import re


class ProgressReader:

    def __init__(self, ip="10.0.0.111", port=8899):
        self.printer_address = (ip, port)
        self.progress = 0

    def get_progress(self):
        return self.progress

    def get_printer_address(self):
        return self.printer_address

    def update_progress(self):
        printer_socket = socket.create_connection(address=self.printer_address, timeout=5)
        # request control
        printer_socket.send('~M601 S1\r\n'.encode())
        printer_socket.recv(1024)
        # request progress
        printer_socket.send('~M27\r\n'.encode())
        data = printer_socket.recv(1024)
        info_result = data.decode()
        # release control
        printer_socket.send('~M602\r\n'.encode())
        printer_socket.recv(1024)
        printer_socket.close()
        # structure response
        regex_groups = re.search('([0-9].*)\/([0-9].*?)\\r', info_result).groups()
        printed, total = regex_groups
        self.progress = 0 if total == 0 else int(float(printed) / int(total) * 100)

    def print_progress(self):
        bar_len = 100
        filled_len = self.progress
        bar = '█' * filled_len + '-' * (bar_len - filled_len)
        sys.stdout.write(f"[{bar}] {self.progress}%\r")
        sys.stdout.flush()
