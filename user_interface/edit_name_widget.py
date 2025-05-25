from data_structures.contact import Contact
from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData, Language, genders
from user_interface.name_component_widget import NameComponentWidget

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

class EditNameWidget:

    def __init__(self, contact: Contact, container, on_update_callback):
        self.contact = contact
        self.container = container
        self.on_update_callback = on_update_callback

        self.initialize(container)


    def initialize(self, container: tk.Frame):
        self.recent_tokens = dict[int, Token]()
        self.recent_tokens = {i: token for i, token in enumerate(self.contact.token_list)}
        self.next_id = len(self.recent_tokens) + 1

        self.recent_meta_data: MetaData = self.contact.meta_data

        self.edit_name_frame = tk.LabelFrame(container, text="Namen und Metadaten anpassen")
        self.edit_name_frame.pack()

        self.render()


    def render(self):

        for widget in self.edit_name_frame.winfo_children():
            widget.destroy()

        for id, token in self.recent_tokens.items():
            NameComponentWidget(
                id=id,
                token=token,
                container=self.edit_name_frame,
                on_update_callback=self.update_token,
                on_delete_callback=self.delete_token
            ).add_component(self.edit_name_frame)

        add_component_button = tk.Button(self.edit_name_frame, text="Komponente hinzufügen", command=self.add_token, bg="#4CA0AF", fg="#000000", activebackground="#1F6E7C", activeforeground="#000000")
        add_component_button.pack(pady=(10, 2))

        # Alter (Age)
        age_frame = tk.Frame(self.edit_name_frame)
        age_frame.pack(pady=(2, 2), fill="x")
        age_frame.columnconfigure(0, weight=1)
        age_frame.columnconfigure(1, weight=1)

        age_label = tk.Label(age_frame, text="Geschätztes Alter:", width=30)
        age_label.grid(row=0, column=0, sticky="ew", padx=(5, 5), pady=5)
        self.age_entry = tk.Entry(age_frame, width=30)
        self.age_entry.grid(row=0, column=1, sticky="ew", padx=(5, 5), pady=5)
        self.age_entry.bind("<KeyRelease>", lambda e: self.update_age(self.age_entry.get()))
        if self.recent_meta_data.estimated_age:
            self.age_entry.insert(0, str(self.recent_meta_data.estimated_age))

        # Sprache (Language)
        language_frame = tk.Frame(self.edit_name_frame)
        language_frame.pack(pady=(2, 2), fill="x")
        language_frame.columnconfigure(0, weight=1)
        language_frame.columnconfigure(1, weight=1)

        language_label = tk.Label(language_frame, text="Sprache:", width=30)
        language_label.grid(row=0, column=0, sticky="ew", padx=(5, 5), pady=5)
        language_entry = ttk.Combobox(language_frame, values=[lang.value for lang in Language], state="readonly", width=30)
        language_entry.grid(row=0, column=1, sticky="ew", padx=(5, 5), pady=5)
        language_entry.bind("<<ComboboxSelected>>", lambda e: self.update_language(language_entry.get()))
        if self.recent_meta_data.language:
            language_entry.set(self.recent_meta_data.language.value)

        # Geschlecht (Gender)
        gender_frame = tk.Frame(self.edit_name_frame)
        gender_frame.pack(pady=(2, 2), fill="x")
        gender_frame.columnconfigure(0, weight=1)
        gender_frame.columnconfigure(1, weight=1)

        gender_label = tk.Label(gender_frame, text="Geschlecht:", width=30)
        gender_label.grid(row=0, column=0, sticky="ew", padx=(5, 5), pady=5)
        gender_entry = ttk.Combobox(gender_frame, values=[g for g in genders], state="readonly", width=30)
        gender_entry.grid(row=0, column=1, sticky="ew", padx=(5, 5), pady=5)
        gender_entry.bind("<<ComboboxSelected>>", lambda e: self.update_gender(gender_entry.get()))
        if self.recent_meta_data.gender:
            gender_entry.set(self.recent_meta_data.gender)

        update_button = tk.Button(self.edit_name_frame, text="Aktualisieren", command=self.update_scanning_state, bg="#4CA0AF", fg="#000000", activebackground="#1F6E7C", activeforeground="#000000")
        update_button.pack(pady=(2, 10))


    def update_token(self, id: int, token: Token):
        if id in self.recent_tokens:
            self.recent_tokens[id] = token


    def delete_token(self, id: int):
        if id in self.recent_tokens:
            del self.recent_tokens[id]

        self.render()


    def add_token(self):
        token = Token(TokenType.LAST_NAME, "")

        self.recent_tokens[self.next_id] = token
        self.next_id += 1

        self.render()

    
    def update_age(self, age: str):
        if age.isdigit():
            self.recent_meta_data.estimated_age = int(age)
        else:
            messagebox.showerror("Ungültiges Alter", "Bitte geben Sie ein gültiges Alter ein (Zahl).")
            self.recent_meta_data.estimated_age = 0
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, str(self.recent_meta_data.estimated_age))


    def update_language(self, language: str):
        self.recent_meta_data.language = Language(language)
        

    def update_gender(self, gender: str):
        self.recent_meta_data.gender = gender


    def update_scanning_state(self):
        contact = Contact(
            token_list=list(self.recent_tokens.values()),
            meta_data=self.recent_meta_data,
        )
        self.on_update_callback(contact)