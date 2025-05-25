import tkinter as tk
import threading
import tkinter.messagebox as messagebox
from data_structures.contact import Contact
from user_interface.ui_elements.loading_animation import LoadingAnimation

class NameScannerWidget:
    def __init__(self, container, scanner, on_new_contact_callback):
        self.scanner = scanner
        self.on_new_contact_callback = on_new_contact_callback
        
        self.contact: Contact = None
        
        self.display(container)


    def display(self, container):
        self.name_scanner_frame = tk.LabelFrame(container, text="Namen erfassen")
        self.name_scanner_frame.pack(padx=10, pady=5)

        self.name_entry = tk.Entry(self.name_scanner_frame, width=30)
        self.name_entry.pack(pady=(10, 0), padx=(10, 10))

        self.capture_button = tk.Button(self.name_scanner_frame, text="Namen erfassen", bg="#DAA36C", fg="#000000", activebackground="#945719", activeforeground="#000000")
        self.capture_button.config(command=lambda: self.submit_name(self.name_entry.get()))
        self.capture_button.pack(pady=(10, 10))

        self.loading_animation = LoadingAnimation(self.name_scanner_frame)



    def submit_name(self, name: str):
        if not name or name.isspace():
            messagebox.showerror("Fehler", "Bitte geben Sie einen gültigen Namen ein.")
            return
        # Name scannen und Meta-Daten aktualisieren
        self.loading_animation.start()
        self.thread = threading.Thread(target=lambda: self._scan_and_finish(name), daemon=True)
        self.thread.start()

    
    def _scan_and_finish(self, name: str):
        self.contact = self.scanner.scan_string(name)
        self.name_scanner_frame.after(0, self._on_scan_finished)

    def _on_scan_finished(self):
        self.loading_animation.stop()
        self.on_new_contact_callback(self.contact)


    def change_input(self, new_contact: Contact):
        self.contact = new_contact
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, new_contact.get_name())