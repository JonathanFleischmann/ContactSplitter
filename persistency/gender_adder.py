from data_structures.meta_data import genders

class GenderAdder:
    def add_gender(self, gender: str) -> None:
        if gender in genders:
            raise ValueError(f"Gender '{gender}' is already known.")
        genders.add(gender)