import tkinter as tk
from tkinter import ttk
from enum import Enum
from persistency.gender_adder import GenderAdder
from persistency.salutations_adder import SalutationAdder
from persistency.title_adder import TitleAdder
from data_structures.meta_data import Language, genders
from scanner.title_scanner import TitleScanner
from scanner.salutation_scanner import SalutationScanner


class EditOptionsWidget:

    def __init__(self, container: tk.Frame, titleScanner: TitleScanner, salutation_scanner: SalutationScanner):
        self.container = container

        self.title_adder = TitleAdder(titleScanner)
        self.gender_adder = GenderAdder()
        self.salutation_adder = SalutationAdder(salutation_scanner)

        self.display(container)

    def display(self, container):
        edit_options_frame = tk.LabelFrame(container, text="Optionen ergänzen")
        edit_options_frame.pack(fill="x", padx=10, pady=5)

        self.title_adder_frame = tk.Frame(edit_options_frame)
        self.title_adder_frame.pack(fill="x", padx=10, pady=5)
        title_label = tk.Label(self.title_adder_frame, text="Titel hinzufügen:")
        title_label.pack(side="left", padx=5, pady=5)
        self.title_adder_entry = ttk.Entry(self.title_adder_frame, width=30)
        self.title_adder_entry.pack(side="left", padx=5, pady=5)
        self.title_adder_language = ttk.Combobox(self.title_adder_frame, values=[l.value for l in Language], state="readonly")
        self.title_adder_language.pack(side="left", padx=5, pady=5)
        self.title_adder_language.set(Language.DE.value)
        title_adder_submit = tk.Button(self.title_adder_frame, text="Hinzufügen")
        title_adder_submit.config(command=lambda: self.add_title())
        title_adder_submit.pack(side="left", padx=5, pady=5)

        self.gender_adder_frame = tk.Frame(edit_options_frame)
        self.gender_adder_frame.pack(fill="x", padx=10, pady=5)
        gender_label = tk.Label(self.gender_adder_frame, text="Gender hinzufügen:")
        gender_label.pack(side="left", padx=5, pady=5)
        self.gender_adder_entry = ttk.Entry(self.gender_adder_frame, width=30)
        self.gender_adder_entry.pack(side="left", padx=5, pady=5)
        gender_adder_submit = tk.Button(self.gender_adder_frame, text="Hinzufügen")
        gender_adder_submit.config(command=lambda: self.add_gender())
        gender_adder_submit.pack(side="left", padx=5, pady=5)

        self.salutation_adder_frame = tk.Frame(edit_options_frame)
        self.salutation_adder_frame.pack(fill="x", padx=10, pady=5)
        salutation_label = tk.Label(self.salutation_adder_frame, text="Anrede hinzufügen:")
        salutation_label.pack(side="left", padx=5, pady=5)
        self.salutation_adder_entry = ttk.Entry(self.salutation_adder_frame, width=30)
        self.salutation_adder_entry.pack(side="left", padx=5, pady=5)
        self.salutation_adder_language = ttk.Combobox(self.salutation_adder_frame, values=[l.value for l in Language], state="readonly")
        self.salutation_adder_language.pack(side="left", padx=5, pady=5)
        self.salutation_adder_language.set(Language.DE.value)
        self.salutation_adder_gender = ttk.Combobox(self.salutation_adder_frame, values=[g for g in genders], state="readonly")
        self.salutation_adder_gender.pack(side="left", padx=5, pady=5)
        self.salutation_adder_gender.set("Nichtbinär")
        salutation_adder_submit = tk.Button(self.salutation_adder_frame, text="Hinzufügen")
        salutation_adder_submit.config(command=lambda: self.add_salutation())
        salutation_adder_submit.pack(side="left", padx=5, pady=5)


    def add_title(self):
        title = self.title_adder_entry.get()
        language = self.title_adder_language.get()
        if title and language:
            self.title_adder.add_title(title, Language(language))
            self.title_adder_entry.delete(0, tk.END)
            self.title_adder_language.set(Language.DE.value)
        else:
            print("Bitte Titel und Sprache angeben.")


    def add_gender(self):
        gender = self.gender_adder_entry.get()
        if gender:
            self.gender_adder.add_gender(gender)
            self.gender_adder_entry.delete(0, tk.END)
            self.clear_container()
            self.display(self.container)
        else:
            print("Bitte Gender angeben.")

    def add_salutation(self):
        salutation = self.salutation_adder_entry.get()
        language = self.salutation_adder_language.get()
        gender = self.salutation_adder_gender.get()
        if salutation and language and gender:
            self.salutation_adder.add_salutation(salutation, Language(language), gender)
            self.salutation_adder_entry.delete(0, tk.END)
            self.salutation_adder_language.set(Language.DE.value)
            self.salutation_adder_gender.set("Nichtbinär")
        else:
            print("Bitte Anrede, Sprache und Gender angeben.")

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        