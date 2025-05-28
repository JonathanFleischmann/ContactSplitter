from data_structures.contact import Contact
from generators.letter_greeting_generator import LetterGreetingGenerator
from data_structures.meta_data import Language
import tkinter as tk
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.text import Text
from user_interface.ui_elements.combobox import Combobox

class LetterGreetingWidget:
    """
    Widget zur Anzeige und Auswahl der Briefanrede für einen Kontakt.
    """

    def __init__(self, contact: Contact, container: tk.Frame, letter_greeting_generator: LetterGreetingGenerator):
        self.contact = contact
        self.letter_greeting_generator = letter_greeting_generator
        self.display(container)

    def display(self, container):
        """Erstellt das UI für die Briefanrede-Ausgabe und Sprachauswahl."""
        letter_salutation_frame = Frame(container, "Briefanrede")
        self.salutation_output = Text(letter_salutation_frame)
        # Combobox zur Auswahl der Sprache
        self.language_combobox = Combobox(
            letter_salutation_frame,
            [l.value for l in Language],
            lambda e: self.set_salutation(Language(self.language_combobox.get_value()))
        )
        self.language_combobox.set_value(self.contact.meta_data.language.value)
        self.set_salutation()

    def set_salutation(self, language: Language = None):
        """Aktualisiert die Briefanrede basierend auf der gewählten Sprache."""
        if language is None:
            language = self.contact.meta_data.language
        salutation = self.letter_greeting_generator.generate(self.contact, language)
        self.salutation_output.update_text(salutation)