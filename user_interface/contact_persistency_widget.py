from persistency.contact_saver import ContactSaver
from data_structures.contact import Contact
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
import tkinter as tk
import tkinter.messagebox as messagebox

class ContactPersistencyWidget:
    def __init__(self, contact_saver: ContactSaver, recent_contact: Contact, container, on_reload_contact_callback):
        self.contact_saver = contact_saver
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
        
        previews = list(self.contact_saver.get_preview_of_all_contacts().items())
        for contact_id, contact_name in reversed(previews):
            Button(self.persistency_frame, text=contact_name, callback_method=lambda cid=contact_id: self.load_contact(cid)).blue()


    def save_contact(self):
        if not self.recent_contact or not self.recent_contact.token_list or not self.recent_contact.meta_data or self.recent_contact.token_list == []:
            messagebox.showinfo("Kontakt speichern", "Es gibt keinen Kontakt zum Speichern. Bitte erfassen Sie zuerst einen Namen.")
            return
        self.contact_saver.save_contact(self.recent_contact);
        self.render()


    def load_contact(self, contact_id: int):
        contact = self.contact_saver.get_contact(contact_id)
        if contact:
            self.recent_contact = contact
            self.on_reload_contact_callback(self.recent_contact)
        else:
            print(f"Kontakt mit ID {contact_id} nicht gefunden.")