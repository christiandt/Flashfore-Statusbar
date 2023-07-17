import json
import socket


class Preferences:

    def __init__(self):
        self.configuration = dict()
        self.filename = "configuration.json"
        self.read_config()
        if self.ip == "auto":
            self.ip = self.search_for_printer()

    def write_config(self):
        with open(self.filename, 'wb') as f:
            f.write(bytes(json.dumps(self.configuration), 'utf-8'))

    def read_config(self):
        with open(self.filename, 'r') as f:
            self.configuration = json.loads(f.read())

    @staticmethod
    def search_for_printer():
        """ Will send a UDP broadcast looking for a Flashforge 3D printer """
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.settimeout(5)
            sock.sendto(bytes("c0a800de46500000", 'utf-8'), ("225.0.0.9", 19000))
            name, address = sock.recvfrom(1024)
            ip, port = address
        return str(ip)

    @property
    def ip(self):
        return str(self.configuration['ip'])

    @ip.setter
    def ip(self, value):
        self.configuration['ip'] = str(value)

    @property
    def interval(self):
        return int(self.configuration['interval'])

    @interval.setter
    def interval(self, value):
        self.configuration['interval'] = int(value)

    @property
    def port(self):
        if 'port' in self.configuration:
            return int(self.configuration['port'])
        return False

    @port.setter
    def port(self, value):
        self.configuration['port'] = int(value)

    @property
    def config(self):
        return self.configuration

    @config.setter
    def config(self, value):
        self.configuration = value


