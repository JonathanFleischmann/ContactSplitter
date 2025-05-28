import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Entry:
    """
    Wrapper für ein Tkinter-Entry-Feld mit optionalem Callback und variabler Breite.
    """

    def __init__(self, parent: Frame, on_key_release_callback=None, in_one_row=False, long_entry=False):
        self.parent = parent
        self.on_key_release_callback = on_key_release_callback
        width = 60 if long_entry else 30

        # Entry-Feld initialisieren
        self.entry = tk.Entry(
            self.parent.frame,
            width=width,
        )
        # Anordnung im UI
        if in_one_row:
            self.entry.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            self.entry.pack(padx=5, pady=5)
            
        # Optionales Key-Release-Callback
        if self.on_key_release_callback:
            self.entry.bind("<KeyRelease>", self.on_key_release_callback)

    def get_value(self):
        """Gibt den aktuellen Wert des Entry-Felds zurück."""
        return self.entry.get()
    
    def set_value(self, value: str):
        """Setzt den Wert des Entry-Felds."""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def clear(self):
        """Löscht den Inhalt des Entry-Felds."""
        self.entry.delete(0, tk.END)