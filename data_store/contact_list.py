from typing import List
from data_structures.contact import Contact
from data_store.database import Database

class ContactList:
    """
    A class to represent a list of contacts.
    """

    def __init__(self):
        self.contacts: List[Contact] = []
        self.database = Database()

    def add_contact(self, contact: Contact) -> None:
        """
        Add a contact to the list.
        """
        self.contacts.append(contact)

    def get_contacts(self) -> List[Contact]:
        """
        Get the list of contacts.
        """
        return self.contacts
    
    def change_contact(self, index: int, contact: Contact) -> None:
        """
        Change a contact in the list.
        """
        if 0 <= index < len(self.contacts):
            self.contacts[index] = contact
        else:
            raise IndexError("Index out of range.")
        
    def delete_contact(self, index: int) -> None:
        """
        Delete a contact from the list.
        """
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
        else:
            raise IndexError("Index out of range.")
        
    def store_persistent(self):
        """
        Store the contact list persistently in the database.
        """
        self.database.save_contacts(self.contacts)

    def load_persistent(self):
        """
        Load the contact list from the database.
        """
        self.contacts = self.database.load_contacts()

