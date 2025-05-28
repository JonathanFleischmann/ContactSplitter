import tkinter as tk
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.text import Text
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.label import Label
from data_structures.contact import Contact
from generators.letter_greeting_generator import LetterGreetingGenerator

class SavedContactWidget:
    """
    Widget zur Anzeige eines gespeicherten Kontakts mit Bearbeiten- und Löschen-Funktion.
    """

    def __init__(self, parent: Frame, contact: Contact, letter_greeting_generator: LetterGreetingGenerator, on_load_callback, on_delete_callback):
        self.parent = parent
        self.contact = contact
        self.letter_greeting_generator = letter_greeting_generator
        self.on_load_callback = on_load_callback
        self.on_delete_callback = on_delete_callback

        self.initialize()

    def initialize(self):
        """Initialisiert das UI für einen gespeicherten Kontakt."""
        self.frame = Frame(self.parent.frame, None, True)
        self.text = Text(self.frame, True, True)
        self.text.update_text(self.contact.get_name())
        
        Button(self.frame, "Bearbeiten", self.load_contact, True, True).blue()
        Button(self.frame, "Löschen", self.delete_contact, True, True).red()

        self.greeting_frame = Frame(self.parent.frame, None, True)
        Label(self.greeting_frame, "Briefanrede:", True, True)
        letter_greeting_text = Text(self.greeting_frame, True, False, True)
        letter_greeting_text.update_text(self.letter_greeting_generator.generate(self.contact))

    def load_contact(self):
        """Lädt den Kontakt (Callback)."""
        self.on_load_callback()

    def delete_contact(self):
        """Löscht den Kontakt (Callback)."""
        self.on_delete_callback()