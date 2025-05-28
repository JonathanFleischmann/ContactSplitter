import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Label:
    """
    Wrapper für ein Tkinter-Label mit optionaler Breite und Anordnung.
    """

    def __init__(self, parent: Frame, text: str, in_one_row=False, slim=False):
        self.parent = parent
        self.text = text
        # Breite je nach 'slim'-Option
        self.width = 15 if slim else 30

        # Label initialisieren
        self.label = tk.Label(
            self.parent.frame,
            text=self.text,
            width=self.width,
        )
        # Anordnung im UI
        if in_one_row:
            self.label.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            self.label.pack(padx=5, pady=5)