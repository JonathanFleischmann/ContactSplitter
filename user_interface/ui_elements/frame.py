import tkinter as tk

class Frame:
    def __init__(self, parent, text=None):
        self.parent = parent
        self.text = text
        if text:
            self.frame = tk.LabelFrame(parent, text=text)
        else:
            self.frame = tk.Frame(parent)
        self.frame.pack(padx=10, pady=10)

    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()