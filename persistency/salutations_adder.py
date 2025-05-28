from data_structures.meta_data import Language, genders
from scanner.salutation_scanner import SalutationScanner


class SalutationAdder:

    salutation_scanner: SalutationScanner

    def __init__(self, salutation_scanner: SalutationScanner):
        self.salutation_scanner = salutation_scanner

    def add_salutation(self, salutation: str, language: Language, gender: str) -> None:
        if salutation in self.salutation_scanner.salutations:
            raise ValueError(f"Salutation already exists in dictionary.")
        if gender not in genders:
            raise ValueError(f"Unknown gender:'{gender}'")
        if salutation == "":
            raise ValueError(f"No empty string allowed.")
        
        self.salutation_scanner.salutations[salutation] = {
            "language": language,
            "gender": gender
        }