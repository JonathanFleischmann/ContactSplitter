import tkinter as tk
from tkinter import ttk
from enum import Enum
from persistency.gender_adder import GenderAdder
from persistency.salutations_adder import SalutationAdder
from persistency.title_adder import TitleAdder
from data_structures.meta_data import Language, genders
from scanner.title_scanner import TitleScanner
from scanner.salutation_scanner import SalutationScanner
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.label import Label
from user_interface.ui_elements.entry import Entry
from user_interface.ui_elements.combobox import Combobox


class EditOptionsWidget:

    def __init__(self, container: tk.Frame, titleScanner: TitleScanner, salutation_scanner: SalutationScanner):
        self.container = container

        self.title_adder = TitleAdder(titleScanner)
        self.gender_adder = GenderAdder()
        self.salutation_adder = SalutationAdder(salutation_scanner)

        self.display(container)

    def display(self, container):
        edit_options_frame = Frame(container, "Optionen ergänzen")

        self.title_adder_frame = Frame(edit_options_frame.frame)
        Label(self.title_adder_frame, "Titel hinzufügen:")
        self.title_adder_entry = Entry(self.title_adder_frame, lambda e: self.add_title())
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


    def add_title(self):
        title = self.title_adder_entry.get_value()
        language = self.title_adder_language.get()
        if title and language:
            self.title_adder.add_title(title, Language(language))
            self.title_adder_entry.clear()
            self.title_adder_language.set(Language.DE.value)
        else:
            print("Bitte Titel und Sprache angeben.")


    def add_gender(self):
        gender = self.gender_adder_entry.get_value()
        if gender:
            self.gender_adder.add_gender(gender)
            self.gender_adder_entry.clear()
            self.clear_container()
            self.display(self.container)
        else:
            print("Bitte Gender angeben.")

    def add_salutation(self):
        salutation = self.salutation_adder_entry.get_value()
        language = self.salutation_adder_language.get_value()
        gender = self.salutation_adder_gender.get_value()
        if salutation and language and gender:
            self.salutation_adder.add_salutation(salutation, Language(language), gender)
            self.salutation_adder_entry.clear()
            self.salutation_adder_language.set_value(Language.DE.value)
            self.salutation_adder_gender.set_value("Nichtbinär")
        else:
            print("Bitte Anrede, Sprache und Gender angeben.")

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        