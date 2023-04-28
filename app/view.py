import tkinter as tk
import tkinter.ttk as ttk


class View:
    def __init__(self, root):
        self.labelText = tk.StringVar()
        self.labelText.set("Test")
        self.root = root
        self.root.title("IoT Platform")
        self.create_view()

    def create_view(self):
        self.label1 = ttk.Label(self.root, textvariable=self.labelText)
        self.label1.grid(row=0, column=0, padx=5, pady=5)

        self.button = ttk.Button(self.root, text="test")
        self.button.grid(row=1, column=0, pady=5, padx=5)

    def updateLabel(self, text : str):
        self.labelText.set("Test updated")
