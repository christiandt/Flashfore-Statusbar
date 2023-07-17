import json


class Preferences:

    def __init__(self):
        self.configuration = dict()
        self.filename = "configuration.json"
        self.read_config()

    def write_config(self):
        with open(self.filename, 'wb') as f:
            f.write(bytes(json.dumps(self.configuration), 'utf-8'))

    def read_config(self):
        with open(self.filename, 'r') as f:
            self.configuration = json.loads(f.read())

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


