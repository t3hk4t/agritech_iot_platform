from tkinter import ttk


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.selected_sensor_index = -1
        self.view.buttons["sensor_add"]["command"] = self.add_fake_sensor
        self.view.listBoxes["sensor_list"].bind("<<ListboxSelect>>", self.on_list_box_select)
        self.view.canvas["main_canvas"].bind('<Button-1>', self.on_canvas_clink)

    def updateData(self):
        self.view.updateLabel(self.model.getMyData())

    def add_fake_sensor(self):
        index, name = self.model.add_dummy_sensor()
        self.view.add_sensor_to_list(index, name)

    def on_list_box_select(self, evt):
        widget = evt.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        split = value.split(":")
        index = int(split[0])
        self.view.open_sensor_list_popup(index, split[1], self.on_delete_sensor, self.on_select_sensor)

    def on_select_sensor(self, root, index):
        self.selected_sensor_index = index
        root.destroy()

    def on_delete_sensor(self, root, index):
        self.view.remove_sensor_from_list(index)
        self.model.remove_dummy_sensor(index)
        root.destroy()

    def on_canvas_clink(self, event):
        x = event.x
        y = event.y

        self.view.draw_oval_on_canvas(self.selected_sensor_index,
                                      x - 5,
                                      x + 5,
                                      y - 5,
                                      y + 5)

    def on_canvas_right_click(self, event):
        pass