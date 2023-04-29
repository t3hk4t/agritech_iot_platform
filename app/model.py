import sqlite3
from sensor import Sensor

class Model:
    def __init__(self):
        self.con = None
        self.cur = None
        self.sensors = {}

    def getMyData(self):
        return "test"

    def search_for_sensors(self):
        pass

    def add_dummy_sensor(self, name:str, id:int):
        self.sensors[id] = Sensor(id, name)

    def get_sensor_data(self, id):
        pass

    def get_sim_sensor_data(self, id):
        if id in self.sensors:
            return self.sensors[id].getData()

