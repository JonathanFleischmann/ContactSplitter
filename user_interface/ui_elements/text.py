import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Text:
    """
    Wrapper für ein nicht-editierbares Tkinter-Textfeld mit verschiedenen Höhenoptionen.
    """

    def __init__(self, parent: Frame, in_one_row=False, flat: bool=False, medium: bool=False):
        self.parent = parent

        # Höhe des Textfelds je nach Option
        if flat:
            height = 1
        elif medium:
            height = 2
        else:
            height = 7

        # Textfeld initialisieren (nicht editierbar)
        self.text = tk.Text(
            self.parent.frame,
            height=height,
            width=50,
            wrap=tk.WORD,
            state="disabled",
            bg="#f7f7f7",
        )
        # Anordnung im UI
        if in_one_row:
            self.text.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            self.text.pack(padx=5, pady=5)

    def update_text(self, content: str):
        """
        Aktualisiert den angezeigten Text.
        """
        self.text.config(state="normal")
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, content)
        self.text.config(state="disabled")