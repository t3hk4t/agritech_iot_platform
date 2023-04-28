from tkinter import ttk


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.button["command"] = self.updateData

    def updateData(self):
        self.view.updateLabel(self.model.getMyData())
