import tkinter as tk
from scanner.scanner import Scanner
from data_structures.contact import Contact
from data_structures.contact import get_empty_contact
from user_interface.name_scanner_widget import NameScannerWidget
from user_interface.letter_salutation_widget import LetterSalutationWidget
from user_interface.edit_name_widget import EditNameWidget
from user_interface.edit_options_widget import EditOptionsWidget
from user_interface.mode_change_widget import ModeChangeWidget, Mode
from user_interface.contact_persistency_widget import ContactPersistencyWidget
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from data_store.contact_list import ContactList




class UserInterface:

    def start_ui(self, scanner: Scanner, contact_list: ContactList, contact: Contact = get_empty_contact()):
        self.root = tk.Tk()
        self.root.title("ContactSplitter")

        self.scanner: Scanner = scanner
        self.contact_list: ContactList = contact_list
        self.title_scanner: TitleScanner = scanner.title_scanner
        self.salutation_scanner: SalutationScanner = scanner.salutation_scanner
        self.contact: Contact = contact

        self.mode = Mode.LETTER_SALUTATION

        self.build_ui()

        self.root.mainloop()

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

        EditNameWidget(self.contact, self.dynamic_frame)

    def switch_to_input_history(self):
        self.clear_dynamic_frame()

        ContactPersistencyWidget(
            self.contact_list,
            self.contact,
            self.dynamic_frame,
            self.update_name,
            self.reset_contact
        )

    def switch_to_edit_options(self):
        self.clear_dynamic_frame()

        EditOptionsWidget(self.dynamic_frame, self.title_scanner, self.salutation_scanner)

    def update_name(self, contact: Contact):
        self.contact = contact

    def reset_contact(self):
        self.contact = self.scanner.get_empty_contact()