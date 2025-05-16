from typing import List
from ContactSplitter.data_structures.contact import Contact

class ContactList:
    """
    A class to represent a list of contacts.
    """

    def __init__(self):
        self.contacts: List[Contact] = []

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

