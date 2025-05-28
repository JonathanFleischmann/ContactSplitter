from data_store.contact_list import ContactList
from data_structures.contact import Contact
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.frame import Frame
from user_interface.saved_contact_widget import SavedContactWidget
from user_interface.ui_elements.custom_info import CustomInfo
from user_interface.ui_elements.custom_ask_yes_no import CustomAskYesNo

class ContactPersistencyWidget:
    def __init__(self, contact_list: ContactList, recent_contact: Contact, container, on_reload_contact_callback, on_save_contact_callback):
        self.contact_list = contact_list
        self.recent_contact = recent_contact
        self.container = container
        self.on_reload_contact_callback = on_reload_contact_callback
        self.on_save_contact_callback = on_save_contact_callback

        self.display()

    def display(self):
        self.persistency_frame = Frame(self.container, "Speichern und Laden")

        self.render()

    def render(self):

        self.persistency_frame.clear()

        Button(self.persistency_frame, text="Kontakt speichern", callback_method=lambda: self.save_contact()).green()
        
        saved_contacts = self.contact_list.get_contacts()
        for index, contact in zip(reversed(range(len(saved_contacts))), reversed(saved_contacts)):
            SavedContactWidget(self.persistency_frame, contact, 
                                on_load_callback=lambda idx=index: self.load_contact(idx),
                                on_delete_callback=lambda idx=index: self.delete_contact(idx))
            
        Button(self.persistency_frame, text="Persistent laden", callback_method=lambda: self.load_contacts_from_disk()).blue()
        Button(self.persistency_frame, text="Persistent speichern", callback_method=lambda: self.save_contacts_to_disk()).blue()


    def save_contact(self):
        if not self.recent_contact or not self.recent_contact.token_list or not self.recent_contact.meta_data or self.recent_contact.token_list == []:
            CustomInfo("Kontakt speichern", "Es gibt keinen Kontakt zum Speichern. Bitte erfassen Sie zuerst einen Namen.")
            return
        self.contact_list.add_contact(self.recent_contact)
        self.render()
        self.on_save_contact_callback()


    def load_contact(self, index: int):
        contact = self.contact_list.get_contacts()[index]
        self.recent_contact = contact
        self.on_reload_contact_callback(self.recent_contact)

    
    def delete_contact(self, index: int):
        if CustomAskYesNo("Kontakt löschen", "Sind Sie sicher, dass Sie diesen Kontakt löschen möchten?").result:
            self.contact_list.delete_contact(index)
            self.render()

    
    def load_contacts_from_disk(self):
        if self.contact_list.load_persistent():
            self.render()
            CustomInfo("Kontakt laden", "Kontakte erfolgreich geladen.")
        else:
            CustomInfo("Kontakt laden", "Keine gespeicherten Kontakte gefunden.")

    def save_contacts_to_disk(self):
        if self.contact_list.store_persistent():
            CustomInfo("Kontakt speichern", "Kontakte erfolgreich gespeichert.")
        else:
            CustomInfo("Kontakt speichern", "Kontakte in der Datenbank wurden geleert.")