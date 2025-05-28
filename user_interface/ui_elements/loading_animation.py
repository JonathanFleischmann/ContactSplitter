import tkinter as tk
from user_interface.ui_elements.frame import Frame

class LoadingAnimation:
    """
    Zeigt eine animierte Ladeanzeige mit Punkten ("Laden...", "Laden..", etc.) an.
    """

    def __init__(self, parent: Frame):
        # Container-Frame für das Label
        self.container = parent.frame
        self.running = False
        self.label = None
        self.dots = 0
        self.increasing = True

    def start(self):
        """Startet die Ladeanimation."""
        if self.running:
            return
        self.running = True
        if not self.label:
            self.label = tk.Label(self.container, text="Laden", width=52, anchor="w")
            self.label.pack(pady=0)
        self.dots = 0
        self.increasing = True
        self._animate()

    def stop(self):
        """Stoppt die Ladeanimation und entfernt das Label."""
        self.running = False
        if self.label:
            self.label.destroy()
            self.label = None

    def _animate(self):
        """Interne Methode zur Animation der Punkte."""
        if not self.running:
            return
        max_dots = 4
        # Text aktualisieren
        self.label.config(text="Laden" + "." * self.dots)
        # Punktezahl erhöhen oder verringern
        if self.increasing:
            if self.dots < max_dots:
                self.dots += 1
            else:
                self.increasing = False
        else:
            if self.dots > 0:
                self.dots -= 1
            else:
                self.increasing = True
        # Nächsten Animationsschritt planen
        self.label.after(100, self._animate)