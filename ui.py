import tkinter as tk
from tkinter import ttk
from scanner.scanner import Scanner
from data_structures.scanning_state import ScanningState, MetaData, Language
from user_interface.name_component_widget import NameComponentWidget
from user_interface.edit_name_widget import EditNameWidget
from user_interface.edit_options_widget import EditOptionsWidget
from user_interface.mode_change_widget import ModeChangeWidget, Mode
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner




class NamensUI:
    def __init__(self, root):

        self.salutation_scanner = SalutationScanner()
        self.title_scanner = TitleScanner()
        name_scanner = NameScanner()
        self.scanner = Scanner(self.salutation_scanner, self.title_scanner, name_scanner)

        meta_data = MetaData()
        meta_data.language = Language.DE
        meta_data.gender = "Unbekannt"

        self.scanning_state = ScanningState(
            token_list=[],
            meta_data=meta_data,
            remaining_name="",
        )

        self.root = root
        self.root.title("ContactSplitter")

        self.mode = Mode.LETTER_SALUTATION

        self.build_ui()

    def build_ui(self):
        # Eingabefeld + Button
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.pack(pady=(10, 2))

        self.capture_button = tk.Button(self.root, text="Namen erfassen")
        self.capture_button.config(command=lambda: self.submit_name(self.name_entry.get()))
        self.capture_button.pack(pady=(0, 10))

        self.dynamic_frame = tk.Frame(self.root)

        ModeChangeWidget(self.root, self.switch_mode)

        # Dynamischer Bereich
        self.dynamic_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Initialer Modus
        self.switch_mode(self.mode)

    def submit_name(self, name: str):
        self.scanning_state = self.scanner.scan_string(name)
        self.switch_mode(self.mode)

    def switch_mode(self, mode: Mode):
        self.mode = mode
        self.clear_dynamic_frame()

        if mode == Mode.LETTER_SALUTATION:
            self.switch_to_briefanrede()
        elif mode == Mode.EDIT_NAME_AND_DATA:
            self.switch_to_edit_name_and_data()
        elif mode == Mode.INPUT_HISTORY:
            pass
        elif mode == Mode.EDIT_OPTIONS:
            self.switch_to_edit_options()

    def clear_dynamic_frame(self):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

    def switch_to_briefanrede(self):
        self.clear_dynamic_frame()

        self.output_label = tk.Label(self.dynamic_frame, text="Briefanrede-Ausgabe:")
        self.output_label.pack(anchor="w")

        self.output_field = tk.Entry(self.dynamic_frame, width=40)
        self.output_field.pack(pady=5)

    def switch_to_edit_name_and_data(self):
        self.clear_dynamic_frame()

        EditNameWidget(self.scanning_state, self.dynamic_frame, self.update_name)

    def switch_to_edit_options(self):
        self.clear_dynamic_frame()

        EditOptionsWidget(self.dynamic_frame, self.title_scanner, self.salutation_scanner)
            
    def update_name(self, scanningState: ScanningState):
        self.scanning_state = scanningState
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, scanningState.get_name())


if __name__ == "__main__":
    root = tk.Tk()
    app = NamensUI(root)
    root.mainloop()