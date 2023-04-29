import sqlite3
from sensor import Sensor


class Model:
    def __init__(self):
        self.con = None
        self.cur = None
        self.canvas_sensors = {}
        self.fake_canvas_sensors = {}

    def getMyData(self):
        return "test"

    def search_for_sensors(self):
        pass

    def add_dummy_sensor(self):
        for index in range(1000):
            if not index in self.fake_canvas_sensors:
                self.fake_canvas_sensors[index] = {
                    "index": index,
                    "name": f"fake_sensor_{index}",
                    "sensor_obj": Sensor(index, f"fake_sensor_{index}")
                }
                return index, f"fake_sensor_{index}"

    def remove_dummy_sensor(self, index):
        if index in self.fake_canvas_sensors:
            del self.fake_canvas_sensors[index]

    def get_sensor_data(self, index):
        if index in self.canvas_sensors:
            return self.canvas_sensors[index]["sensor_obj"].get_data()

    def get_sim_sensor_data(self, index):
        if index in self.fake_canvas_sensors:
            return self.fake_canvas_sensors[index]["sensor_obj"].get_data()

    def get_sim_sensor_name(self, index):
        if index in self.fake_canvas_sensors:
            return self.fake_canvas_sensors[index]["name"]

    def get_sim_sensor_ip(self, index):
        if index in self.fake_canvas_sensors:
            return self.fake_canvas_sensors[index]["sensor_obj"].get_ip()
