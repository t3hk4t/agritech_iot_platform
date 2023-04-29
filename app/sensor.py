import random


class Sensor:
    def __init__(self, sensor_id: int, name: str):
        self.id = sensor_id,
        self.name = name

    def connect(self):
        pass

    def __get_raw_data(self):
        return random.randint(0, 1024)

    def get_data(self):
        return self.__get_raw_data()
