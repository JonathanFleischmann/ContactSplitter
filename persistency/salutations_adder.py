from data_structures.meta_data import Language, genders


class SalutationAdder:
    def __init__(self, salutation_scanner):
        self.salutation_scanner = salutation_scanner

    def add_salutation(self, salutation: str, language: Language, gender: str) -> None:
        if salutation in self.salutation_scanner.salutations:
            raise ValueError(f"Salutation '{salutation}' already exists in dictionary.")
        if gender not in genders:
            raise ValueError(f"Unknown gender:'{gender}'")
        
        self.salutation_scanner.salutations[salutation] = {
            "language": language,
            "gender": gender
        }