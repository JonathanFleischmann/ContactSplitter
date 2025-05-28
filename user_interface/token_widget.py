from data_structures.token import Token, TokenType
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.entry import Entry
from user_interface.ui_elements.combobox import Combobox

import tkinter as tk

class TokenWidget:
    """
    Widget zur Bearbeitung eines einzelnen Token (Wert und Typ) mit Entfernen-Button.
    """

    def __init__(self, id, token: Token, container: tk.Frame, on_delete_callback):
        self.id = id
        self.token = token
        self.on_delete_callback = on_delete_callback

    def add_component(self, container: tk.Frame) -> tk.Frame:
        """
        Fügt die UI-Komponenten für das Token zum Container hinzu.
        """
        frame = Frame(container)
        self.token_value_entry = Entry(frame, lambda e: self.update_token_value(), True)
        self.token_type_entry = Combobox(
            frame,
            [t.value for t in TokenType if t != TokenType.SALUTATION],
            lambda e: self.change_token_type(),
            True
        )
        Button(frame, "Entfernen", lambda: self.delete(), True).red()

        self.token_value_entry.set_value(self.token.value)
        self.token_type_entry.set_value(self.token.type.value)

    def update_token_value(self):
        """
        Aktualisiert den Wert des Tokens aus dem Entry-Feld.
        """
        new_value = self.token_value_entry.get_value()
        self.token.value = new_value

    def change_token_type(self):
        """
        Ändert den Typ des Tokens entsprechend der Auswahl in der Combobox.
        """
        selected_type = self.token_type_entry.get_value()
        self.token.type = TokenType(selected_type)

    def delete(self):
        """
        Ruft den Callback zum Löschen des Tokens auf.
        """
        self.on_delete_callback(self.id)