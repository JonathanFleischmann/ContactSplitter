import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Entry:
    def __init__(self, parent: Frame, on_key_release_callback=None, in_one_row=False):
        self.parent = parent
        self.on_key_release_callback = on_key_release_callback

        self.entry = tk.Entry(
            self.parent.frame,
            width=30
        )
        if in_one_row:
            self.entry.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            self.entry.pack(padx=5, pady=5)
            
        if self.on_key_release_callback:
            self.entry.bind("<KeyRelease>", self.on_key_release_callback)

    def get_value(self):
        return self.entry.get()
    
    def set_value(self, value: str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def clear(self):
        self.entry.delete(0, tk.END)