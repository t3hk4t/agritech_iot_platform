from tkinter import Tk

from controller import Controller
from model import Model
from view import View

if __name__ == '__main__':
    root = Tk()
    view = View(root)
    model = Model()
    controller = Controller(model, view)
    root.mainloop()