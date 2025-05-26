import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Text:
    def __init__(self, parent: Frame):
        self.parent = parent
        self.text = tk.Text(
            self.parent.frame,
            height=5,
            width=50,
            wrap=tk.WORD,
            state="normal",
            bg="#f7f7f7",
        )
        self.text.pack(padx=5, pady=5)

    def update_text(self, content: str):
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, content)