import tkinter as tk
from enum import Enum

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
        mode_frame = tk.LabelFrame(container, text="Modus")
        mode_frame.pack(padx=10, pady=5)

        letter_salutation_button = tk.Button(mode_frame, text=Mode.LETTER_SALUTATION.value, bg="#7C4CAF", fg="#FFFFFF", activebackground="#4E138D", activeforeground="#FFFFFF")
        letter_salutation_button.config(command=lambda: self.on_mode_change_callback(Mode.LETTER_SALUTATION))
        letter_salutation_button.pack(side="left", padx=5, pady=5)

        edit_name_and_data_button = tk.Button(mode_frame, text=Mode.EDIT_NAME_AND_DATA.value, bg="#7C4CAF", fg="#FFFFFF", activebackground="#4E138D", activeforeground="#FFFFFF")
        edit_name_and_data_button.config(command=lambda: self.on_mode_change_callback(Mode.EDIT_NAME_AND_DATA))
        edit_name_and_data_button.pack(side="left", padx=5, pady=5)

        input_history_button = tk.Button(mode_frame, text=Mode.INPUT_HISTORY.value, bg="#7C4CAF", fg="#FFFFFF", activebackground="#4E138D", activeforeground="#FFFFFF")
        input_history_button.config(command=lambda: self.on_mode_change_callback(Mode.INPUT_HISTORY))
        input_history_button.pack(side="left", padx=5, pady=5)

        edit_options_button = tk.Button(mode_frame, text=Mode.EDIT_OPTIONS.value, bg="#7C4CAF", fg="#FFFFFF", activebackground="#4E138D", activeforeground="#FFFFFF")
        edit_options_button.config(command=lambda: self.on_mode_change_callback(Mode.EDIT_OPTIONS))
        edit_options_button.pack(side="left", padx=5, pady=5)
        