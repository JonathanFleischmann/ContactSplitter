from data_structures.meta_data import Language, genders
from generators.letter_greeting_generator import LetterGreetingGenerator

class LetterGreetingAdder:

    letter_greeting_generator: LetterGreetingGenerator

    def __init__(self, letter_greeting_generator: LetterGreetingGenerator):
        self.letter_greeting_generator = letter_greeting_generator

    def add_salutation(self, greeting: str, language: Language, gender: str, include_name: bool) -> None:
        if gender not in genders:
            raise ValueError(f"Unknown gender:'{gender}'")
        if greeting == "":
            raise ValueError(f"No empty string allowed.")
        
        self.letter_greeting_generator.greetings[greeting] = {
            "language": language,
            "gender": gender
        }
        self.letter_greeting_generator.include_name[greeting] = include_name