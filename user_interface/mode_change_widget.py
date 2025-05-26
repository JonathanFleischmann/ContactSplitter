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

    def __init__(self, container: tk.Frame, on_mode_change_callback):
        self.container = container
        self.on_mode_change_callback = on_mode_change_callback

        self.initialize(container)

    def initialize(self, container):
        mode_frame = Frame(container, "Modus")
        Button(mode_frame, Mode.LETTER_SALUTATION.value, lambda: self.on_mode_change_callback(Mode.LETTER_SALUTATION), True).purple()
        Button(mode_frame, Mode.EDIT_NAME_AND_DATA.value, lambda: self.on_mode_change_callback(Mode.EDIT_NAME_AND_DATA), True).purple()
        Button(mode_frame, Mode.INPUT_HISTORY.value, lambda: self.on_mode_change_callback(Mode.INPUT_HISTORY), True).purple()
        Button(mode_frame, Mode.EDIT_OPTIONS.value, lambda: self.on_mode_change_callback(Mode.EDIT_OPTIONS), True).purple()
        