import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Text:
    def __init__(self, parent: Frame, in_one_row=False, flat: bool=False):
        self.parent = parent

        height = 7

        if flat:
            height = 1

        self.text = tk.Text(
            self.parent.frame,
            height=height,
            width=50,
            wrap=tk.WORD,
            state="normal",
            bg="#f7f7f7",
        )
        if in_one_row:
            self.text.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            self.text.pack(padx=5, pady=5)



    def update_text(self, content: str):
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, content)