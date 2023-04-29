import threading


class Scanner:

    def __init__(self, on_sensor_found, config):
        self.on_sensor_found = on_sensor_found
        self.config = config
        self.connected_devices = {}

    def init(self):
        # Todo: do something with config
        pass

    def run(self):
        while True:
            pass

    def check_device(self):
        pass