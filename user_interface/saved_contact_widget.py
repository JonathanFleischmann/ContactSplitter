import tkinter as tk
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.text import Text
from user_interface.ui_elements.button import Button
from data_structures.contact import Contact

class SavedContactWidget:
    def __init__(self, parent: Frame, contact: Contact, on_load_callback, on_delete_callback):
        self.parent = parent
        self.contact = contact
        self.on_load_callback = on_load_callback
        self.on_delete_callback = on_delete_callback

        self.initialize()
        

    def initialize(self):
        self.frame = Frame(self.parent.frame)
        self.text = Text(self.frame, True, True)
        self.text.update_text(self.contact.get_name())
        
        Button(self.frame, "Bearbeiten", lambda: self.load_contact(), True, True).blue()
        Button(self.frame, "Löschen", lambda: self.delete_contact(), True, True).red()
        
        
    def load_contact(self):
        self.on_load_callback()

    def delete_contact(self):
        self.on_delete_callback()