from data_structures.token import Token, TokenType

import tkinter as tk
from tkinter import ttk

class NameComponentWidget:

    def __init__(self, id, token: Token, container: tk.Frame, on_update_callback, on_delete_callback):
        self.id = id
        self.token = token
        self.on_update_callback = on_update_callback
        self.on_delete_callback = on_delete_callback

    def add_component(self, container: tk.Frame) -> tk.Frame:
        frame = tk.Frame(container)
        frame.pack(fill="x", pady=2)

        self.token_value_entry = ttk.Entry(frame)
        self.token_value_entry.pack(side="left", fill="x", expand=True)
        self.token_value_entry.bind("<KeyRelease>", lambda e: self.update_token_value())

        self.token_type_entry = ttk.Combobox(frame, values=[t.value for t in TokenType], state="readonly")
        self.token_type_entry.pack(side="left", fill="x", expand=True)
        self.token_type_entry.bind("<<ComboboxSelected>>", lambda e: self.change_token_type())

        token_delete_button = tk.Button(frame, text="Entfernen", command=lambda: self.delete())
        token_delete_button.pack(side="left", padx=5)
        token_delete_button.bind("<Enter>", lambda e: token_delete_button.config(bg="red"))
        token_delete_button.bind("<Leave>", lambda e: token_delete_button.config(bg="SystemButtonFace"))
        token_delete_button.bind("<Button-1>", lambda e: self.on_delete_callback(self.id))

        self.token_value_entry.insert(0, self.token.value)
        self.token_type_entry.set(self.token.type.value)

        return frame

    def update_token_value(self):
        new_value = self.token_value_entry.get()
        self.token.value = new_value
        self.on_update_callback(self.id, self.token)

    def change_token_type(self):
        selected_type = self.token_type_entry.get()
        self.token.type = TokenType(selected_type)
        self.on_update_callback(self.id, self.token)

    def delete(self):
        self.on_delete_callback(self.id)
        