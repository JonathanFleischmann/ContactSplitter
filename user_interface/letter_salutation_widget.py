from data_structures.contact import Contact
from generators.letter_greeting_generator import LetterGreetingGenerator
from data_structures.meta_data import Language
import tkinter as tk
from tkinter import ttk

class LetterSalutationWidget:
    def __init__(self, contact: Contact, container: tk.Frame):
        self.contact = contact
        self.letter_greeting_generator = LetterGreetingGenerator()

        self.display(container)

    def display(self, container):
        letter_salutation_frame = tk.LabelFrame(container, text="Briefanrede:")
        letter_salutation_frame.pack(padx=10, pady=5)

        self.salutation_output = tk.Text(letter_salutation_frame, height=5, width=50, wrap=tk.WORD, state="disabled", bg="#f7f7f7")
        self.salutation_output.pack(padx=10, pady=5)
        self.salutation_output.config(state="normal")

        self.title_adder_language = ttk.Combobox(letter_salutation_frame, values=[l.value for l in Language], state="readonly")
        self.title_adder_language.pack(side="left", padx=10, pady=10)
        self.title_adder_language.set(self.contact.meta_data.language.value)
        self.title_adder_language.bind("<<ComboboxSelected>>", lambda e: self.set_salutation(Language(self.title_adder_language.get())))

        self.set_salutation()

    def set_salutation(self, language: Language = None):
        if language is None:
            language = self.contact.meta_data.language
        salutation = self.letter_greeting_generator.generate(self.contact, language)
        self.salutation_output.delete(1.0, tk.END)
        self.salutation_output.insert(tk.END, salutation)