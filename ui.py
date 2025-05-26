import tkinter as tk
from scanner.scanner import Scanner
from data_structures.scanning_state import MetaData, Language, Contact
from user_interface.name_scanner_widget import NameScannerWidget
from user_interface.letter_salutation_widget import LetterSalutationWidget
from user_interface.edit_name_widget import EditNameWidget
from user_interface.edit_options_widget import EditOptionsWidget
from user_interface.mode_change_widget import ModeChangeWidget, Mode
from user_interface.contact_persistency_widget import ContactPersistencyWidget
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner
from persistency.contact_saver import ContactSaver


class NamensUI:
    def __init__(self, root):
        self.salutation_scanner = SalutationScanner()
        self.title_scanner = TitleScanner()
        name_scanner = NameScanner()
        self.scanner = Scanner(self.salutation_scanner, self.title_scanner, name_scanner)
        
        self.contact_saver = ContactSaver()

        meta_data = MetaData()
        meta_data.language = Language.DE
        meta_data.gender = "Divers"
        meta_data.estimated_age = 0

        self.contact = Contact(
            token_list=[],
            meta_data=meta_data
        )

        self.root = root
        self.root.title("ContactSplitter")

        self.mode = Mode.LETTER_SALUTATION

        self.build_ui()

    def build_ui(self):
        
        self.name_scanner_widget: NameScannerWidget = NameScannerWidget(self.root, self.scanner, self.display_contact)


        self.dynamic_frame = tk.Frame(self.root)

        ModeChangeWidget(self.root, self.switch_mode)

        self.dynamic_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Initialer Modus
        self.switch_mode(self.mode)


    def display_contact(self, contact: Contact):
        
        self.contact = contact

        self.switch_mode(self.mode)
                


    def switch_mode(self, mode: Mode):
        self.mode = mode
        self.clear_dynamic_frame()

        if mode == Mode.LETTER_SALUTATION:
            self.switch_to_briefanrede()
        elif mode == Mode.EDIT_NAME_AND_DATA:
            self.switch_to_edit_name_and_data()
        elif mode == Mode.INPUT_HISTORY:
            self.switch_to_input_history()
        elif mode == Mode.EDIT_OPTIONS:
            self.switch_to_edit_options()

    def clear_dynamic_frame(self):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

    def switch_to_briefanrede(self):
        self.clear_dynamic_frame()

        LetterSalutationWidget(self.contact, self.dynamic_frame)

    def switch_to_edit_name_and_data(self):
        self.clear_dynamic_frame()

        EditNameWidget(self.contact, self.dynamic_frame, self.update_name)

    def switch_to_input_history(self):
        self.clear_dynamic_frame()

        ContactPersistencyWidget(
            self.contact_saver,
            self.contact,
            self.dynamic_frame,
            self.update_name
        )

    def switch_to_edit_options(self):
        self.clear_dynamic_frame()

        EditOptionsWidget(self.dynamic_frame, self.title_scanner, self.salutation_scanner)

    def update_name(self, contact: Contact):
        self.contact = contact
        self.name_scanner_widget.change_input(contact)


if __name__ == "__main__":
    root = tk.Tk()
    app = NamensUI(root)
    root.mainloop()