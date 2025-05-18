from data_structures.scanning_state import ScanningState
import tkinter as tk
from tkinter import ttk

class LetterSalutationWidget:
    def __init__(self, ScanningState: ScanningState, container: tk.Frame):
        self.scanning_state = ScanningState

    def display(self):
        print(f"Salutation: {self.salutation}")

    def set_salutation(self, new_salutation):
        self.salutation = new_salutation
        print(f"Salutation updated to: {self.salutation}")