
import json
from data_structures.token import Token, TokenType
from data_structures.meta_data import Language, genders , convert_string_to_language
from data_structures.scanning_state import ScanningState

class SalutationScanner:

    file_path = 'dictionary_data/salutations.json'

    def __init__(self):

        self.salutations : dict[str, dict[Language, str]] = {}

        with open(self.file_path, 'r', encoding='utf-8') as file:
            loaded_salutations = json.load(file)
            self.salutations = {
                key: {
                    "language": convert_string_to_language(value["lang"]),
                    "gender": value["gender"]
                }
                for key, value in loaded_salutations.items()
            }


    
    def scan_salutation(self, scanning_state: ScanningState) -> ScanningState:
        first_word = scanning_state.remaining_name.split(' ')[0]

        if first_word not in self.salutations:
            raise ValueError(f"Salutation '{first_word}' not found in dictionary.")
        
        scanning_state.update( 
            ' '.join(scanning_state.remaining_name.split(' ')[1:]),
            Token(TokenType.SALUTATION, first_word),
            self.salutations[first_word]["language"],
            self.salutations[first_word]["gender"]
            )
        
        
    


    def next_word_salutation(self, scanning_state: ScanningState) -> bool:

        return scanning_state.remaining_name.split(' ')[0] in self.salutations
        