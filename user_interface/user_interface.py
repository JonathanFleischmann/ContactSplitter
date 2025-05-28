import tkinter as tk
from scanner.scanner import Scanner
from generators.letter_greeting_generator import LetterGreetingGenerator
from data_structures.contact import Contact, get_empty_contact
from user_interface.name_scanner_widget import NameScannerWidget
from user_interface.letter_greeting_widget import LetterGreetingWidget
from user_interface.edit_name_widget import EditNameWidget
from user_interface.edit_options_widget import EditOptionsWidget
from user_interface.mode_change_widget import ModeChangeWidget, Mode
from user_interface.contact_persistency_widget import ContactPersistencyWidget
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from data_store.contact_list import ContactList

class UserInterface:
    """
    Hauptklasse für die Benutzeroberfläche der Anwendung.
    Steuert die Anzeige und den Wechsel zwischen den verschiedenen Widgets.
    """

    def start_ui(self, scanner: Scanner, letter_greeting_generator: LetterGreetingGenerator, contact_list: ContactList, contact: Contact = get_empty_contact()):
        self.root = tk.Tk()
        self.root.title("ContactSplitter")

        self.scanner: Scanner = scanner
        self.letter_greeting_generator: LetterGreetingGenerator = letter_greeting_generator
        self.contact_list: ContactList = contact_list
        self.title_scanner: TitleScanner = scanner.title_scanner
        self.salutation_scanner: SalutationScanner = scanner.salutation_scanner
        self.contact: Contact = contact

        self.mode = Mode.LETTER_SALUTATION

        self.build_ui()
        self.root.mainloop()

    def build_ui(self):
        """Initialisiert die Hauptstruktur der UI."""
        self.name_scanner_widget: NameScannerWidget = NameScannerWidget(self.root, self.scanner, self.display_contact)
        self.dynamic_frame = tk.Frame(self.root)
        ModeChangeWidget(self.root, self.switch_mode)
        self.dynamic_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.switch_mode(self.mode)  # Initialer Modus

    def display_contact(self, contact: Contact):
        """Aktualisiert den aktuellen Kontakt und wechselt ggf. die Ansicht."""
        self.contact = contact
        self.switch_mode(self.mode)

    def switch_mode(self, mode: Mode):
        """Wechselt den aktuellen Modus und zeigt das entsprechende Widget."""
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
        """Entfernt alle Widgets aus dem dynamischen Frame."""
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

    def switch_to_briefanrede(self):
        """Zeigt das Widget für die Briefanrede an."""
        self.clear_dynamic_frame()
        LetterGreetingWidget(self.contact, self.dynamic_frame, self.letter_greeting_generator)

    def switch_to_edit_name_and_data(self):
        """Zeigt das Widget zur Bearbeitung von Namen und Daten an."""
        self.clear_dynamic_frame()
        EditNameWidget(self.contact, self.dynamic_frame)

    def switch_to_input_history(self):
        """Zeigt das Widget zur Verwaltung gespeicherter Kontakte an."""
        self.clear_dynamic_frame()
        ContactPersistencyWidget(
            self.contact_list,
            self.contact,
            self.letter_greeting_generator,
            self.dynamic_frame,
            self.update_name,
            self.reset_contact
        )

    def switch_to_edit_options(self):
        """Zeigt das Widget zum Hinzufügen von Optionen an."""
        self.clear_dynamic_frame()
        EditOptionsWidget(self.dynamic_frame, self.title_scanner, self.salutation_scanner, self.letter_greeting_generator)

    def update_name(self, contact: Contact):
        """Aktualisiert den aktuellen Kontakt."""
        self.contact = contact

    def reset_contact(self):
        """Setzt den aktuellen Kontakt auf leer zurück."""
        self.contact = get_empty_contact()