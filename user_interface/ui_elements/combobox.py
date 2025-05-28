import tkinter as tk
from tkinter import ttk
from user_interface.ui_elements.frame import Frame

class Combobox:
    def __init__(self, parent: Frame, options: list, on_select_callback=None, in_one_row=False):
        self.parent = parent
        self.options = options
        self.on_select_callback = on_select_callback

        self.combobox = ttk.Combobox(
            self.parent.frame,
            values=self.options,
            state="readonly",
            width=30
        )
        if in_one_row:
            self.combobox.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            self.combobox.pack(padx=5, pady=5)
        
        if self.on_select_callback:
            self.combobox.bind("<<ComboboxSelected>>", self.on_select_callback)

    def get_value(self):
        return self.combobox.get()
    
    def set_value(self, value: str):
        if value in self.options:
            self.combobox.set(value)
        else:
            raise ValueError(f"Value '{value}' not in options")
        
    def add_option(self, option: str):
        if option not in self.options:
            self.options.append(option)
            self.combobox['values'] = self.options