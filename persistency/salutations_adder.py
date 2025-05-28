from data_structures.meta_data import Language, genders
from scanner.salutation_scanner import SalutationScanner

class SalutationAdder:
    """
    Klasse zum Hinzufügen neuer Anreden zum Anreden-Wörterbuch.
    """

    def __init__(self, salutation_scanner: SalutationScanner):
        self.salutation_scanner = salutation_scanner

    def add_salutation(self, salutation: str, language: Language, gender: str) -> None:
        """
        Fügt eine neue Anrede mit Sprache und Gender hinzu.
        Löst eine Exception aus, wenn die Anrede leer ist, das Gender unbekannt ist oder die Anrede bereits existiert.
        """
        if salutation in self.salutation_scanner.salutations:
            raise ValueError("Salutation already exists in dictionary.")
        if gender not in genders:
            raise ValueError(f"Unknown gender:'{gender}'")
        if salutation == "":
            raise ValueError("No empty string allowed.")
        
        self.salutation_scanner.salutations[salutation] = {
            "language": language,
            "gender": gender
        }