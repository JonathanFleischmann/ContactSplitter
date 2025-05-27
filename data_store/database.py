from tinydb import TinyDB
from typing import List
from dataclasses import asdict
from data_structures.contact import Contact
from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData, Language

class Database:

    def __init__(self, db_path="contacts.json"):
        self.db_path = db_path
        self.db = TinyDB(self.db_path)
        self.table = self.db.table("contacts")

    def contact_to_json(self, contact: Contact) -> dict:
        data = asdict(contact)
        for token in data["token_list"]:
            token["type"] = token["type"].value
        if data["meta_data"]["language"]:
            data["meta_data"]["language"] = data["meta_data"]["language"].value
        return data

    def contact_from_json(self, data: dict) -> Contact:
        tokens = [Token(TokenType(token["type"]), token["value"]) for token in data["token_list"]]
        meta = data["meta_data"]
        meta_data = MetaData()
        meta_data.gender = meta.get("gender")
        meta_data.language = Language(meta["language"]) if meta.get("language") else None
        return Contact(tokens, meta_data)

    def save_contacts(self, contacts: List[Contact]) -> None:
        """Speichert eine Liste von Kontakten in der Datenbank (überschreibt alte Einträge)."""
        self.table.truncate()  # löscht alle alten Einträge
        for contact in contacts:
            self.table.insert(self.contact_to_json(contact))

    def load_contacts(self) -> List[Contact]:
        """Liest alle Kontakte aus der Datenbank und gibt sie als Liste von Contact-Objekten zurück."""
        return [self.contact_from_json(item) for item in self.table.all()]