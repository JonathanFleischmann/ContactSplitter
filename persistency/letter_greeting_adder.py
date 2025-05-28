from data_structures.meta_data import Language, genders
from generators.letter_greeting_generator import LetterGreetingGenerator

class LetterGreetingAdder:
    """
    Klasse zum Hinzufügen neuer Briefanreden zum Briefanreden-Wörterbuch.
    """

    letter_greeting_generator: LetterGreetingGenerator

    def __init__(self, letter_greeting_generator: LetterGreetingGenerator):
        self.letter_greeting_generator = letter_greeting_generator

    def add_salutation(self, greeting: str, language: Language, gender: str, include_name: bool) -> None:
        """
        Fügt eine neue Briefanrede mit Sprache, Gender und Nachnamen-Option hinzu.
        Löst eine Exception aus, wenn das Gender unbekannt ist oder die Anrede leer ist.
        """
        if gender not in genders:
            raise ValueError(f"Unknown gender:'{gender}'")
        if greeting == "":
            raise ValueError("No empty string allowed.")
        
        self.letter_greeting_generator.greetings[greeting] = {
            "lang": language,
            "gender": gender
        }
        self.letter_greeting_generator.include_name[greeting] = include_name