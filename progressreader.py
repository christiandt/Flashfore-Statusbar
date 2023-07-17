# -*- coding: utf-8 -*-

import socket
import sys
import re


class ProgressReader:

    def __init__(self, ip="10.0.0.111", port=8899):
        self.printer_address = {'ip': ip, 'port': port}
        self.progress = 0

    def get_progress(self):
        return self.progress

    def get_printer_address(self):
        return self.printer_address

    def update_progress(self):
        self._send_and_receive(self.printer_address, '~M601 S1\r\n')
        info_result = self._send_and_receive(self.printer_address, '~M27\r\n')
        regex_groups = re.search('([0-9].*)\/([0-9].*?)\\r', info_result).groups()
        printed = int(regex_groups[0])
        total = int(regex_groups[1])
        self.progress = 0 if total == 0 else int(float(printed) / total * 100)

    def print_progress(self):
        bar_len = 100
        filled_len = self.progress
        bar = '█' * filled_len + '-' * (bar_len - filled_len)
        sys.stdout.write(f"[{bar}] {self.progress}%\r")
        sys.stdout.flush()

    @staticmethod
    def _send_and_receive(printer_address, message_data):
        printer_socket = socket.socket()
        printer_socket.settimeout(5)
        printer_socket.connect((printer_address['ip'], printer_address['port']))
        printer_socket.send(message_data.encode())
        data = printer_socket.recv(1024)
        printer_socket.close()
        return data.decode()
