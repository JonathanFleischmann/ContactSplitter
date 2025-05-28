import tkinter as tk
from tkinter import ttk
from data_structures.meta_data import Language, genders
from persistency.gender_adder import GenderAdder
from persistency.salutations_adder import SalutationAdder
from persistency.letter_greeting_adder import LetterGreetingAdder
from persistency.title_adder import TitleAdder
from scanner.title_scanner import TitleScanner
from scanner.salutation_scanner import SalutationScanner
from generators.letter_greeting_generator import LetterGreetingGenerator
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.label import Label
from user_interface.ui_elements.entry import Entry
from user_interface.ui_elements.combobox import Combobox
from user_interface.ui_elements.custom_info import CustomInfo
from core import translate_message_to_german

class EditOptionsWidget:
    """
    Widget zur Ergänzung von Titeln, Gender, Anreden und Briefanreden.
    """

    def __init__(self, container: tk.Frame, titleScanner: TitleScanner, salutation_scanner: SalutationScanner, letter_greeting_generator: LetterGreetingGenerator):
        self.container = container

        self.title_adder = TitleAdder(titleScanner)
        self.gender_adder = GenderAdder()
        self.salutation_adder = SalutationAdder(salutation_scanner)
        self.letter_greeting_adder = LetterGreetingAdder(letter_greeting_generator)

        self.display(container)

    def display(self, container):
        """Erstellt das UI für das Hinzufügen von Optionen."""
        edit_options_frame = Frame(container, "Optionen ergänzen")

        # Titel hinzufügen
        Label(edit_options_frame, "Titel hinzufügen:")
        title_adder_frame = Frame(edit_options_frame.frame, None, True)
        self.title_adder_entry = Entry(title_adder_frame, None, True)
        self.title_adder_language = Combobox(title_adder_frame, [l.value for l in Language], None, True)
        self.title_adder_language.set_value(Language.DE.value)
        Button(edit_options_frame, "Hinzufügen", lambda: self.add_title()).blue()

        # Gender hinzufügen
        Label(edit_options_frame, "Gender hinzufügen:")
        gender_adder_frame = Frame(edit_options_frame.frame, None, True)
        self.gender_adder_entry = Entry(gender_adder_frame)
        Button(edit_options_frame, "Hinzufügen", lambda: self.add_gender()).blue()

        # Anrede hinzufügen
        Label(edit_options_frame, "Anrede hinzufügen:")
        salutation_adder_frame = Frame(edit_options_frame.frame, None, True)
        self.salutation_adder_entry = Entry(salutation_adder_frame, None, True)
        self.salutation_adder_language = Combobox(salutation_adder_frame, [l.value for l in Language], None, True)
        self.salutation_adder_language.set_value(Language.DE.value)
        self.salutation_adder_gender = Combobox(salutation_adder_frame, [g for g in genders], None, True)
        self.salutation_adder_gender.set_value("Nichtbinär")
        Button(edit_options_frame, "Hinzufügen", lambda: self.add_salutation()).blue()

        # Briefanrede hinzufügen
        Label(edit_options_frame, "Briefanrede hinzufügen:")
        letter_greeting_adder_frame = Frame(edit_options_frame.frame, None, True)
        self.letter_greeting_adder_entry = Entry(letter_greeting_adder_frame, None, True)
        self.letter_greeting_adder_language = Combobox(letter_greeting_adder_frame, [l.value for l in Language], None, True)
        self.letter_greeting_adder_language.set_value(Language.DE.value)
        self.letter_greeting_adder_gender = Combobox(letter_greeting_adder_frame, [g for g in genders], None, True)
        self.letter_greeting_adder_gender.set_value("Nichtbinär")
        self.letter_greeting_adder_append_last_name = Combobox(letter_greeting_adder_frame, ["Nachnamen anhängen", "keinen Nachnamen anhängen"], None, True)
        self.letter_greeting_adder_append_last_name.set_value("Nachnamen anhängen")
        Button(edit_options_frame, "Hinzufügen", lambda: self.add_letter_greeting()).blue()

    def add_title(self):
        """Fügt einen neuen Titel hinzu."""
        title = self.title_adder_entry.get_value()
        language = self.title_adder_language.get_value()

        if title == "":
            CustomInfo("Titel hinzufügen", "Bitte geben Sie einen Titel ein.")
            return
        
        try: 
            self.title_adder.add_title(title, Language(language))
        except ValueError as e:
            CustomInfo("Titel hinzufügen", translate_message_to_german(str(e)))
            return

        self.title_adder_entry.clear()
        self.title_adder_language.set_value(Language.DE.value)
        CustomInfo("Titel hinzufügen", f"Der Titel '{title}' wurde erfolgreich hinzugefügt.")

    def add_gender(self):
        """Fügt ein neues Gender hinzu."""
        gender = self.gender_adder_entry.get_value()

        if gender == "":
            CustomInfo("Gender hinzufügen", "Bitte geben Sie ein Gender ein.")
            return
        
        try:
            self.gender_adder.add_gender(gender)
        except ValueError as e:
            CustomInfo("Gender hinzufügen", translate_message_to_german(str(e)))
            return
                       
        self.gender_adder_entry.clear()
        self.salutation_adder_gender.add_option(gender)
        self.letter_greeting_adder_gender.add_option(gender)
        CustomInfo("Gender hinzufügen", f"Das Gender '{gender}' wurde erfolgreich hinzugefügt.")

    def add_salutation(self):
        """Fügt eine neue Anrede hinzu."""
        salutation = self.salutation_adder_entry.get_value()
        language = self.salutation_adder_language.get_value()
        gender = self.salutation_adder_gender.get_value()

        if salutation == "":
            CustomInfo("Anrede hinzufügen", "Bitte geben Sie eine Anrede ein.")
            return
        
        try:
            self.salutation_adder.add_salutation(salutation, Language(language), gender)
        except ValueError as e:
            CustomInfo("Anrede hinzufügen", translate_message_to_german(str(e)))
            return
        
        self.salutation_adder_entry.clear()
        self.salutation_adder_language.set_value(Language.DE.value)
        self.salutation_adder_gender.set_value("Nichtbinär")
        CustomInfo("Anrede hinzufügen", f"Die Anrede '{salutation}' wurde erfolgreich hinzugefügt.")

    def add_letter_greeting(self):
        """Fügt eine neue Briefanrede hinzu."""
        letter_greeting = self.letter_greeting_adder_entry.get_value()
        language = self.letter_greeting_adder_language.get_value()
        gender = self.letter_greeting_adder_gender.get_value()
        append_last_name = self.letter_greeting_adder_append_last_name.get_value()

        if letter_greeting == "":
            CustomInfo("Briefanrede hinzufügen", "Bitte geben Sie eine Briefanrede ein.")
            return
        
        append_last_name = append_last_name == "Nachnamen anhängen"

        try:
            self.letter_greeting_adder.add_salutation(letter_greeting, Language(language), gender, append_last_name)
        except ValueError as e:
            CustomInfo("Briefanrede hinzufügen", translate_message_to_german(str(e)))
            return

        self.letter_greeting_adder_entry.clear()
        self.letter_greeting_adder_language.set_value(Language.DE.value)
        self.letter_greeting_adder_gender.set_value("Nichtbinär")
        self.letter_greeting_adder_append_last_name.set_value("Nachnamen anhängen")
        CustomInfo("Briefanrede hinzufügen", f"Die Briefanrede '{letter_greeting}' wurde erfolgreich hinzugefügt.")

    def clear_container(self):
        """Leert das Container-Widget."""
        for widget in self.container.winfo_children():
            widget.destroy()