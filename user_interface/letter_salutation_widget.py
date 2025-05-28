from data_structures.contact import Contact
from generators.letter_greeting_generator import LetterGreetingGenerator
from data_structures.meta_data import Language
import tkinter as tk
from tkinter import ttk
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.text import Text
from user_interface.ui_elements.combobox import Combobox

class LetterSalutationWidget:
    def __init__(self, contact: Contact, container: tk.Frame, letter_greeting_generator: LetterGreetingGenerator):
        self.contact = contact
        self.letter_greeting_generator: LetterGreetingGenerator = letter_greeting_generator

        self.display(container)

    def display(self, container):

        letter_salutation_frame = Frame(container, "Briefanrede")
        self.salutation_output = Text(letter_salutation_frame)
        title_adder_language = Combobox(letter_salutation_frame, [l.value for l in Language], lambda e: self.set_salutation(Language(title_adder_language.get_value())))
        title_adder_language.set_value(self.contact.meta_data.language.value)

        self.set_salutation()

    def set_salutation(self, language: Language = None):
        if language is None:
            language = self.contact.meta_data.language
        salutation = self.letter_greeting_generator.generate(self.contact, language)
        self.salutation_output.update_text(salutation)