from tkinter import ttk


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.sim_sensor_counter = 0
        self.view.buttons["sensor_add"]["command"] = self.add_fake_sensor

    def updateData(self):
        self.view.updateLabel(self.model.getMyData())

    def add_fake_sensor(self):
        self.model.add_dummy_sensor("dummy_sensor", self.sim_sensor_counter)
        self.sim_sensor_counter += 1
        self.view.add_sensor_to_list(self.sim_sensor_counter-1, "dummy_sensor")