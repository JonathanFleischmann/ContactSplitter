import tkinter as tk
import threading
import tkinter.messagebox as messagebox
from data_structures.contact import Contact
from user_interface.ui_elements.loading_animation import LoadingAnimation
from user_interface.ui_elements.frame import Frame
from user_interface.ui_elements.button import Button
from user_interface.ui_elements.entry import Entry
from user_interface.ui_elements.checkbox import Checkbox
from core import translate_message_to_german

class NameScannerWidget:
    def __init__(self, container, scanner, on_new_contact_callback):
        self.scanner = scanner
        self.on_new_contact_callback = on_new_contact_callback
        
        self.contact: Contact = None
        
        self.display(container)


    def display(self, container):
        self.name_scanner_frame = Frame(container, "Namen scannen")

        self.name_entry = Entry(self.name_scanner_frame, None, False, True)

        self.use_ai = Checkbox(self.name_scanner_frame, "Gender mit KI ermitteln", None, False)
        self.use_ai.set_value(True)

        Button(self.name_scanner_frame, "Namen scannen", lambda: self.submit_name(self.name_entry.get_value())).orange()

        self.loading_animation = LoadingAnimation(self.name_scanner_frame)




    def submit_name(self, name: str):
        if not name or name.isspace():
            messagebox.showerror("Fehler", "Bitte geben Sie einen gültigen Namen ein.")
            return
        use_ai = self.use_ai.get_value()
        # Name scannen und Meta-Daten aktualisieren
        self.loading_animation.start()
        self.thread = threading.Thread(target=lambda: self._scan_and_finish(name, use_ai), daemon=True)
        self.thread.start()

    
    def _scan_and_finish(self, name: str, use_ai: bool = False):
        try:
            self.contact = self.scanner.scan_string(name, use_ai)
        except Exception as e:
            self.loading_animation.stop()
            messagebox.showerror("Fehler", f"Der Name konnte nicht gescannt werden: {translate_message_to_german(str(e))}")
            return
        self.name_scanner_frame.frame.after(0, self._on_scan_finished)

    def _on_scan_finished(self):
        self.loading_animation.stop()
        self.on_new_contact_callback(self.contact)
        self.name_entry.set_value('')