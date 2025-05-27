from data_store.contact_list import ContactList
from data_structures.contact import Contact
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
import tkinter as tk
import tkinter.messagebox as messagebox

class ContactPersistencyWidget:
    def __init__(self, contact_list: ContactList, recent_contact: Contact, container, on_reload_contact_callback):
        self.contact_list = contact_list
        self.recent_contact = recent_contact
        self.container = container
        self.on_reload_contact_callback = on_reload_contact_callback

        self.display()

    def display(self):
        self.persistency_frame = Frame(self.container, "Speichern und Laden")

        self.render()

    def render(self):

        self.persistency_frame.clear()

        Button(self.persistency_frame, text="Kontakt speichern", callback_method=lambda: self.save_contact()).green()
        
        saved_contacts = self.contact_list.get_contacts()
        for contact in reversed(saved_contacts):
            Button(self.persistency_frame, text=contact.get_name(), callback_method=lambda cont=contact: self.load_contact(cont)).blue()


    def save_contact(self):
        if not self.recent_contact or not self.recent_contact.token_list or not self.recent_contact.meta_data or self.recent_contact.token_list == []:
            messagebox.showinfo("Kontakt speichern", "Es gibt keinen Kontakt zum Speichern. Bitte erfassen Sie zuerst einen Namen.")
            return
        self.contact_list.add_contact(self.recent_contact);
        self.render()


    def load_contact(self, contact: Contact):
        self.recent_contact = contact
        self.on_reload_contact_callback(self.recent_contact)