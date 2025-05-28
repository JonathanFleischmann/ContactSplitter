import tkinter as tk
from enum import Enum
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame

class Mode(Enum):
    LETTER_SALUTATION = "Briefanrede"
    EDIT_NAME_AND_DATA = "Namen und Daten anpassen"
    INPUT_HISTORY = "Eingabeverlauf"
    EDIT_OPTIONS = "Optionen ergänzen"

class ModeChangeWidget:
    """
    Widget zur Auswahl des aktuellen Modus der Anwendung.
    """

    def __init__(self, container: tk.Frame, on_mode_change_callback):
        self.container = container
        self.on_mode_change_callback = on_mode_change_callback
        self.initialize(container)

    def initialize(self, container):
        """Erstellt die Buttons zur Modusauswahl."""
        mode_frame = Frame(container, "Modus")
        for mode in Mode:
            Button(
                mode_frame,
                mode.value,
                lambda m=mode: self.on_mode_change_callback(m),
                True
            ).purple()