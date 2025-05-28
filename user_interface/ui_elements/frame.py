import tkinter as tk

class Frame:
    def __init__(self, parent, text=None, small_margin=False):
        self.parent = parent
        self.text = text
        if text:
            self.frame = tk.LabelFrame(parent, text=text)
        else:
            self.frame = tk.Frame(parent)
        if small_margin:
            self.frame.pack(padx=2, pady=2)
        else:      
            self.frame.pack(padx=10, pady=10)

    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()