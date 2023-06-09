import tkinter as tk
import tkinter.ttk as ttk
import json


class View:
    def __init__(self, root: tk.Tk, config_path: str):
        # configure root
        self.root = root
        self.root.title("IoT Platform")
        self.root.resizable(False, False)
        # configure frames
        self.canvasFrame = ttk.Frame(self.root)
        self.canvasFrame.grid(row=0, column=0, sticky=tk.N)
        self.canvasFrame.columnconfigure(0, weight=1)
        self.canvasFrame.columnconfigure(1, weight=1)
        self.canvasFrame.rowconfigure(0, weight=1)
        self.canvasFrame.rowconfigure(1, weight=1)
        self.sensorFrame = ttk.Frame(self.root)
        self.sensorFrame.grid(row=0, column=1, sticky=tk.N)
        self.sensorFrame.columnconfigure(0, weight=1)
        self.sensorFrame.columnconfigure(1, weight=1)
        self.sensorFrame.rowconfigure(0, weight=1)
        self.sensorFrame.rowconfigure(1, weight=1)
        # configure widget contrainers
        self.canvas = {}
        self.listBoxes = {}
        self.scrollBars = {}
        self.labels = {}
        self.buttons = {}
        self.sensor_drawings = {}
        # load config
        raw_file = open(config_path)
        self.view_config = json.load(raw_file)
        self.create_view(self.view_config)

    def create_view(self, config: dict):
        if not "widgets" in config:
            print("Error: missing widgets in config!")
            raise AssertionError

        widgets = config["widgets"]
        for widget in widgets:
            if widget == "Canvas":
                for canvas in widgets[widget]:
                    frame = None
                    if widgets[widget][canvas]["frame"] == "canvas":
                        frame = self.canvasFrame
                    else:
                        frame = self.sensorFrame

                    self.canvas[canvas] = tk.Canvas(
                        frame,
                        bg=widgets[widget][canvas]["default_color"],
                        width=widgets[widget][canvas]["width"],
                        height=widgets[widget][canvas]["height"]
                    )
                    self.canvas[canvas].grid(
                        row=widgets[widget][canvas]["row"],
                        column=widgets[widget][canvas]["column"],
                        rowspan=widgets[widget][canvas]["row_span"],
                        columnspan=widgets[widget][canvas]["column_span"],
                        padx=widgets[widget][canvas]["pad_x"],
                        pady=widgets[widget][canvas]["pad_y"],
                        sticky=widgets[widget][canvas]["sticky"]
                    )
            if widget == "Listbox":
                for list_box in widgets[widget]:
                    frame = None
                    if widgets[widget][list_box]["frame"] == "canvas":
                        frame = self.canvasFrame
                    else:
                        frame = self.sensorFrame

                    self.listBoxes[list_box] = tk.Listbox(
                        self.sensorFrame,
                        width=widgets[widget][list_box]["width"],
                        height=widgets[widget][list_box]["height"]
                    )
                    self.listBoxes[list_box].grid(
                        row=widgets[widget][list_box]["row"],
                        column=widgets[widget][list_box]["column"],
                        padx=widgets[widget][list_box]["pad_x"],
                        pady=widgets[widget][list_box]["pad_y"],
                        sticky=widgets[widget][list_box]["sticky"]
                    )
            if widget == "Button":
                for button in widgets[widget]:
                    frame = None
                    if widgets[widget][button]["frame"] == "canvas":
                        frame = self.canvasFrame
                    else:
                        frame = self.sensorFrame

                    self.buttons[button] = ttk.Button(
                        frame,
                        text=widgets[widget][button]["text"],
                        width=25
                    )
                    self.buttons[button].grid(
                        row=widgets[widget][button]["row"],
                        column=widgets[widget][button]["column"],
                        rowspan=widgets[widget][button]["row_span"],
                        columnspan=widgets[widget][button]["column_span"],
                        padx=widgets[widget][button]["pad_x"],
                        pady=widgets[widget][button]["pad_y"],
                        sticky=widgets[widget][button]["sticky"]
                    )

            if widget == "Label":
                for label in widgets[widget]:
                    frame = None
                    if widgets[widget][label]["frame"] == "canvas":
                        frame = self.canvasFrame
                    else:
                        frame = self.sensorFrame

                    self.labels[label] = ttk.Label(
                        frame,
                        text=widgets[widget][label]["text"],
                        width=100,
                        borderwidth=1,
                        relief="solid",
                        justify=tk.CENTER
                    )
                    self.labels[label].grid(
                        row=widgets[widget][label]["row"],
                        column=widgets[widget][label]["column"],
                        rowspan=widgets[widget][label]["row_span"],
                        columnspan=widgets[widget][label]["column_span"],
                        padx=widgets[widget][label]["pad_x"],
                        pady=widgets[widget][label]["pad_y"],
                        sticky=widgets[widget][label]["sticky"]
                    )

    def add_sensor_to_list(self, id: int, name: str):
        self.listBoxes["sensor_list"].insert(tk.END, f"{id}:{name}")

    def remove_sensor_from_list(self, index):
        self.listBoxes["sensor_list"].delete(index)

    def open_sensor_list_popup(self, index, name, on_delete, on_save):
        sensor_list_popup = tk.Toplevel(self.root)
        sensor_list_popup.title(f"{index}:{name}")

        button1 = ttk.Button(sensor_list_popup, text="Delete",
                             command=lambda: on_delete(sensor_list_popup, index))
        button1.grid(row=0, column=0)
        button2 = ttk.Button(sensor_list_popup, text="Select",
                             command=lambda: on_save(sensor_list_popup, index))
        button2.grid(row=0, column=1)

    def draw_oval_on_canvas(self, index, x0, x1, y0, y1, is_sim = True):
        if index == -1:
            return
        if not index in self.sensor_drawings:
            self.sensor_drawings[index] = {
                "canvas_obj": self.canvas["main_canvas"].create_oval(x0, y0, x1, y1, fill="black"),
                'canvas_name_obj': self.canvas["main_canvas"].create_text(x0, y0 - 5, text=str(index)),
                "x0": x0,
                "x1": x1,
                "y0": y0,
                "y1": y1,
            }
        else:
            self.canvas["main_canvas"].delete(self.sensor_drawings[index]["canvas_obj"])
            self.canvas["main_canvas"].delete(self.sensor_drawings[index]["canvas_name_obj"])
            del self.sensor_drawings[index]
            self.sensor_drawings[index] = {
                "canvas_obj": self.canvas["main_canvas"].create_oval(x0, y0, x1, y1, fill="black"),
                'canvas_name_obj': self.canvas["main_canvas"].create_text(x0, y0 - 5, text=str(index)),
                "x0": x0,
                "x1": x1,
                "y0": y0,
                "y1": y1,
            }

    def get_drawn_sensor_index(self, x, y):
        for sensor in self.sensor_drawings:
            if self.sensor_drawings[sensor]["x0"] <= x <= self.sensor_drawings[sensor]["x1"]:
                if self.sensor_drawings[sensor]["y0"] <= y <= self.sensor_drawings[sensor]["y1"]:
                    return sensor

        return -1

    def sensor_dev_info_popup(self,index, name, config : dict):
        sensor_info_popup = tk.Toplevel(self.root)
        sensor_info_popup.title(f"{index}:{name}")
        for count, key in enumerate(config):
            label = ttk.Label(sensor_info_popup, text=config[key])
            label.grid(row=count, column=0)
