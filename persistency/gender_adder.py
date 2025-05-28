from data_structures.meta_data import genders

class GenderAdder:
    """
    Klasse zum Hinzufügen neuer Gender zum Gender-Set.
    """

    def add_gender(self, gender: str) -> None:
        """
        Fügt ein neues Gender hinzu.
        Löst eine Exception aus, wenn das Gender leer ist oder bereits existiert.
        """
        if gender in genders:
            raise ValueError("Gender is already known.")
        if gender == "":
            raise ValueError("No empty string allowed.")
        
        genders.add(gender)