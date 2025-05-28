import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Label:
    def __init__(self, parent: Frame, text: str, in_one_row=False, slim=False):
        self.parent = parent
        self.text = text
        self.width = 30

        if slim:
            self.width = 15

        self.label = tk.Label(
            self.parent.frame,
            text=self.text,
            width=self.width,
        )
        if in_one_row:
            self.label.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            self.label.pack(padx=5, pady=5)