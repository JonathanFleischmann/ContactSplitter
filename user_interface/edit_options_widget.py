import tkinter as tk
from tkinter import ttk
from enum import Enum
from persistency.gender_adder import GenderAdder
from persistency.salutations_adder import SalutationAdder
from persistency.letter_greeting_adder import LetterGreetingAdder
from persistency.title_adder import TitleAdder
from data_structures.meta_data import Language, genders
from scanner.title_scanner import TitleScanner
from scanner.salutation_scanner import SalutationScanner
from generators.letter_greeting_generator import LetterGreetingGenerator
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.label import Label
from user_interface.ui_elements.entry import Entry
from user_interface.ui_elements.combobox import Combobox
from user_interface.ui_elements.custom_info import CustomInfo

class EditOptionsWidget:

    def __init__(self, container: tk.Frame, titleScanner: TitleScanner, salutation_scanner: SalutationScanner, letter_greeting_generator: LetterGreetingGenerator):
        self.container = container

        self.title_adder = TitleAdder(titleScanner)
        self.gender_adder = GenderAdder()
        self.salutation_adder = SalutationAdder(salutation_scanner)
        self.letter_greeting_adder = LetterGreetingAdder(letter_greeting_generator)

        self.display(container)

    def display(self, container):
        edit_options_frame = Frame(container, "Optionen ergänzen")

        self.title_adder_frame = Frame(edit_options_frame.frame)
        Label(self.title_adder_frame, "Titel hinzufügen:")
        self.title_adder_entry = Entry(self.title_adder_frame)
        self.title_adder_language = Combobox(self.title_adder_frame, [l.value for l in Language])
        self.title_adder_language.set_value(Language.DE.value)
        Button(self.title_adder_frame, "Hinzufügen", lambda: self.add_title()).blue()

        gender_adder_frame = Frame(edit_options_frame.frame)
        Label(gender_adder_frame, "Gender hinzufügen:")
        self.gender_adder_entry = Entry(gender_adder_frame)
        Button(gender_adder_frame, "Hinzufügen", lambda: self.add_gender()).blue()

        salutation_adder_frame = Frame(edit_options_frame.frame)
        Label(salutation_adder_frame, "Anrede hinzufügen:")
        self.salutation_adder_entry = Entry(salutation_adder_frame)
        self.salutation_adder_language = Combobox(salutation_adder_frame, [l.value for l in Language])
        self.salutation_adder_language.set_value(Language.DE.value)
        self.salutation_adder_gender = Combobox(salutation_adder_frame, [g for g in genders])
        self.salutation_adder_gender.set_value("Nichtbinär")
        Button(salutation_adder_frame, "Hinzufügen", lambda: self.add_salutation()).blue()

        letter_greeting_adder_frame = Frame(edit_options_frame.frame)
        Label(letter_greeting_adder_frame, "Briefanrede hinzufügen:")
        self.letter_greeting_adder_entry = Entry(letter_greeting_adder_frame)
        self.letter_greeting_adder_language = Combobox(letter_greeting_adder_frame, [l.value for l in Language])
        self.letter_greeting_adder_language.set_value(Language.DE.value)
        self.letter_greeting_adder_gender = Combobox(letter_greeting_adder_frame, [g for g in genders])
        self.letter_greeting_adder_gender.set_value("Nichtbinär")
        self.letter_greeting_adder_append_last_name = Combobox(letter_greeting_adder_frame, [b for b in ["Nachnamen anhängen", "keinen Nachnamen anhängen"]])
        self.letter_greeting_adder_append_last_name.set_value("Nachnamen anhängen")
        Button(letter_greeting_adder_frame, "Hinzufügen", lambda: self.add_letter_greeting()).blue()


    def add_title(self):
        title = self.title_adder_entry.get_value()
        language = self.title_adder_language.get_value()

        if title == "":
            CustomInfo("Titel hinzufügen", "Bitte geben Sie einen Titel ein.")
            return
        
        self.title_adder.add_title(title, Language(language))
        self.title_adder_entry.clear()
        self.title_adder_language.set_value(Language.DE.value)

        CustomInfo("Titel hinzufügen", f"Der Titel '{title}' wurde erfolgreich hinzugefügt.")


    def add_gender(self):
        gender = self.gender_adder_entry.get_value()

        if gender == "":
            CustomInfo("Gender hinzufügen", "Bitte geben Sie ein Gender ein.")
            return

        self.gender_adder.add_gender(gender)
        self.gender_adder_entry.clear()
        self.clear_container()
        self.display(self.container)

        CustomInfo("Gender hinzufügen", f"Der Titel '{gender}' wurde erfolgreich hinzugefügt.")
                   

    def add_salutation(self):
        salutation = self.salutation_adder_entry.get_value()
        language = self.salutation_adder_language.get_value()
        gender = self.salutation_adder_gender.get_value()

        if salutation == "":
            CustomInfo("Anrede hinzufügen", "Bitte geben Sie eine Anrede ein.")
            return
        
        self.salutation_adder.add_salutation(salutation, Language(language), gender)
        self.salutation_adder_entry.clear()
        self.salutation_adder_language.set_value(Language.DE.value)
        self.salutation_adder_gender.set_value("Nichtbinär")

        CustomInfo("Anrede hinzufügen", f"Die Anrede '{salutation}' wurde erfolgreich hinzugefügt.")


    def add_letter_greeting(self):
        letter_greeting = self.letter_greeting_adder_entry.get_value()
        language = self.letter_greeting_adder_language.get_value()
        gender = self.letter_greeting_adder_gender.get_value()
        append_last_name = self.letter_greeting_adder_append_last_name.get_value()
        if letter_greeting == "":
            CustomInfo("Briefanrede hinzufügen", "Bitte geben Sie eine Briefanrede ein.")
            return
        
        append_last_name = True if append_last_name == "Nachnamen anhängen" else False

        self.letter_greeting_adder.add_salutation(letter_greeting, Language(language), gender, append_last_name)

        self.letter_greeting_adder_entry.clear()
        self.letter_greeting_adder_language.set_value(Language.DE.value)
        self.letter_greeting_adder_gender.set_value("Nichtbinär")
        self.letter_greeting_adder_append_last_name.set_value("Nachnamen anhängen")


        CustomInfo("Briefanrede hinzufügen", f"Die Briefanrede '{letter_greeting}' wurde erfolgreich hinzugefügt.")


    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        