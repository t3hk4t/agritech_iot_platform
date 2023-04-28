from tkinter import Tk
from tkinter import ttk
import os

from controller import Controller
from model import Model
from view import View

if __name__ == '__main__':
    root = Tk()
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    view = View(root, "." + os.sep + "app_config.json")
    model = Model()
    controller = Controller(model, view)
    root.mainloop()