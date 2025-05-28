from data_structures.contact import Contact
from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData, Language, genders
from user_interface.token_widget import TokenWidget
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.label import Label
from user_interface.ui_elements.combobox import Combobox

import tkinter as tk
import tkinter.messagebox as messagebox

class EditNameWidget:
    """
    Widget zur Bearbeitung eines Kontaktnamens und zugehöriger Metadaten.
    """

    def __init__(self, contact: Contact, container):
        self.contact = contact
        self.container = container
        self.initialize(container)

    def initialize(self, container: tk.Frame):
        # Tokens und Metadaten initialisieren
        self.recent_tokens = {i: token for i, token in enumerate(self.contact.token_list)}
        self.next_id = len(self.recent_tokens) + 1
        self.recent_meta_data: MetaData = self.contact.meta_data
        self.edit_name_frame = Frame(container, "Name bearbeiten")
        self.render()

    def render(self):
        """Rendert das Bearbeitungs-UI für Tokens und Metadaten."""
        self.edit_name_frame.clear()

        # Tokens anzeigen
        for id, token in self.recent_tokens.items():
            TokenWidget(
                id=id,
                token=token,
                container=self.edit_name_frame.frame,
                on_delete_callback=lambda id=id: self.delete_token(id),
            ).add_component(self.edit_name_frame.frame)

        # Button zum Hinzufügen neuer Token
        Button(self.edit_name_frame, "Komponente hinzufügen", lambda: self.add_token()).blue()

        # Sprache (Language)
        language_frame = Frame(self.edit_name_frame.frame)
        Label(language_frame, "Sprache:", True)
        language_entry = Combobox(
            language_frame,
            [lang.value for lang in Language],
            lambda e: self.update_language(language_entry.get_value()),
            True
        )
        if self.recent_meta_data.language:
            language_entry.set_value(self.recent_meta_data.language.value)

        # Geschlecht (Gender)
        gender_frame = Frame(self.edit_name_frame.frame)
        Label(gender_frame, "Geschlecht:", True)
        gender_entry = Combobox(
            gender_frame,
            [g for g in genders],
            lambda e: self.update_gender(gender_entry.get_value()),
            True
        )
        if self.recent_meta_data.gender:
            gender_entry.set_value(self.recent_meta_data.gender)

    def update_token(self, id: int, token: Token):
        """Aktualisiert einen Token anhand der ID."""
        if id in self.recent_tokens:
            self.recent_tokens[id] = token

    def delete_token(self, id: int):
        """Löscht einen Token anhand der ID und aktualisiert die Anzeige."""
        if id in self.recent_tokens:
            del self.recent_tokens[id]
        self.contact.token_list = list(self.recent_tokens.values())
        self.render()

    def add_token(self):
        """Fügt einen neuen Token hinzu und aktualisiert die Anzeige."""
        token = Token(TokenType.LAST_NAME, "")
        self.recent_tokens[self.next_id] = token
        self.next_id += 1
        self.contact.token_list = list(self.recent_tokens.values())
        self.render()

    def update_age(self, age: str):
        """Aktualisiert das Alter in den Metadaten."""
        if age.isdigit():
            self.recent_meta_data.estimated_age = int(age)
        else:
            messagebox.showerror("Ungültiges Alter", "Bitte geben Sie ein gültiges Alter ein (Zahl).")
            self.recent_meta_data.estimated_age = 0
        self.age_entry.set_value(self.recent_meta_data.estimated_age)

    def update_language(self, language: str):
        """Aktualisiert die Sprache in den Metadaten."""
        self.recent_meta_data.language = Language(language)

    def update_gender(self, gender: str):
        """Aktualisiert das Geschlecht in den Metadaten."""
        self.recent_meta_data.gender = gender