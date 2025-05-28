import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Checkbox:
    """
    Wrapper für ein Tkinter-Checkbox-Element mit Callback-Unterstützung.
    """

    def __init__(self, parent: Frame, text: str, on_change_callback=None, in_one_row=False):
        self.parent = parent
        self.on_change_callback = on_change_callback

        # BooleanVar für den Status der Checkbox
        self.var = tk.BooleanVar(value=False)
        # Checkbox initialisieren
        self.checkbox = tk.Checkbutton(
            self.parent.frame,
            text=text,
            variable=self.var,
            command=self._on_change
        )
        # Anordnung im UI
        if in_one_row:
            self.checkbox.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            self.checkbox.pack(padx=5, pady=5)

    def _on_change(self):
        """Callback bei Statusänderung der Checkbox."""
        if self.on_change_callback:
            self.on_change_callback(self.var.get())
    
    def set_value(self, value: bool):
        """Setzt den Wert der Checkbox."""
        self.var.set(value)

    def get_value(self) -> bool:
        """Gibt den aktuellen Wert der Checkbox zurück."""
        return self.var.get()