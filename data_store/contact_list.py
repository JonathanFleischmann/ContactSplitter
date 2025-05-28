from typing import List
from data_structures.contact import Contact
from data_store.database import Database

class ContactList:
    """
    Klasse zur Verwaltung einer Kontaktliste mit Persistenz.
    """

    def __init__(self):
        self.contacts: List[Contact] = []
        self.database = Database()

    def add_contact(self, contact: Contact) -> None:
        """Fügt einen Kontakt zur Liste hinzu."""
        self.contacts.append(contact)

    def get_contacts(self) -> List[Contact]:
        """Gibt die Liste der Kontakte zurück."""
        return self.contacts
    
    def change_contact(self, index: int, contact: Contact) -> None:
        """Ändert einen Kontakt an gegebener Position."""
        if 0 <= index < len(self.contacts):
            self.contacts[index] = contact
        else:
            raise IndexError("Index out of range.")
        
    def delete_contact(self, index: int) -> None:
        """Löscht einen Kontakt aus der Liste."""
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
        else:
            raise IndexError("Index out of range.")
        
    def store_persistent(self) -> bool:
        """Speichert die Kontaktliste persistent in der Datenbank."""
        self.database.save_contacts(self.contacts)
        return bool(self.contacts)

    def load_persistent(self) -> bool:
        """Lädt die Kontaktliste aus der Datenbank."""
        contacts = self.database.load_contacts()
        if not contacts:
            return False
        self.contacts = contacts
        return True