from persistency.contact_saver import ContactSaver
from data_structures.contact import Contact
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
        self.persistency_frame = tk.LabelFrame(self.container, text="Speichern und Laden")
        self.persistency_frame.pack(padx=10, pady=5)

        self.render()

    def render(self):
        max_len = 30

        for widget in self.persistency_frame.winfo_children():
            widget.destroy()

        self.save_button = tk.Button(
            self.persistency_frame,
            text="Kontakt speichern",
            bg="#4CAF50",
            fg="white",
            activebackground="#388E3C",
            activeforeground="white",
            width=max_len
        )
        self.save_button.config(command=lambda: self.save_contact())
        self.save_button.pack(padx=5, pady=(5, 15))

        # Kontakte in umgekehrter Reihenfolge anzeigen
        previews = list(self.contact_saver.get_preview_of_all_contacts().items())
        for contact_id, contact_name in reversed(previews):
            # Text ggf. abkürzen
            contact_button = tk.Button(
                self.persistency_frame, 
                text=contact_name, 
                bg="#4CA0AF",
                fg="#000000",
                activebackground="#1F6E7C",
                activeforeground="#000000",
                width=max_len, 
                anchor="w")
            contact_button.config(command=lambda cid=contact_id: self.load_contact(cid))
            contact_button.pack(padx=5, pady=2)


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