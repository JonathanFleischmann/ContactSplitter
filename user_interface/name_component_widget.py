from data_structures.token import Token, TokenType
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.entry import Entry
from user_interface.ui_elements.combobox import Combobox

import tkinter as tk
from tkinter import ttk

class NameComponentWidget:

    def __init__(self, id, token: Token, container: tk.Frame, on_update_callback, on_delete_callback):
        self.id = id
        self.token = token
        self.on_update_callback = on_update_callback
        self.on_delete_callback = on_delete_callback

    def add_component(self, container: tk.Frame) -> tk.Frame:
        frame = Frame(container)
        self.token_value_entry = Entry(frame, lambda e: self.update_token_value(), True)
        self.token_type_entry = Combobox(frame, [t.value for t in TokenType], lambda e: self.change_token_type(), True)
        Button(frame, "Entfernen", lambda: self.on_delete_callback(), True).red()

        self.token_value_entry.set_value(self.token.value)
        self.token_type_entry.set_value(self.token.type.value)

    def update_token_value(self):
        new_value = self.token_value_entry.get_value()
        self.token.value = new_value
        self.on_update_callback(self.id, self.token)

    def change_token_type(self):
        selected_type = self.token_type_entry.get_value()
        self.token.type = TokenType(selected_type)
        self.on_update_callback(self.id, self.token)

    def delete(self):
        self.on_delete_callback(self.id)
        