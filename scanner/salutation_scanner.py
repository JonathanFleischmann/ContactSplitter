
import json
from data_structures.token import Token, TokenType
from data_structures.meta_data import Language, Gender, convert_string_to_language, convert_string_to_gender
from data_structures.scanning_state import ScanningState

class SalutationScanner:

    file_path = 'dictionary_data/salutations.json'

    def __init__(self):

        self.salutations : dict[str, dict[Language, Gender]] = {}

        with open(self.file_path, 'r', encoding='utf-8') as file:
            loaded_salutations = json.load(file)
            self.salutations = {
                key: {
                    "language": convert_string_to_language(value["lang"]),
                    "gender": convert_string_to_gender(value["gender"])
                }
                for key, value in loaded_salutations.items()
            }


    
    def scan_salutation(self, scanning_state: ScanningState) -> ScanningState:
        first_word = scanning_state.remaining_name.split(' ')[0]

        if first_word in self.salutations:

            if scanning_state.has_salutation():
                raise ValueError(f"Multiple salutations found")
            
            token = Token(TokenType.SALUTATION, first_word)

            scanning_state.token_list.append(token)
            scanning_state.remaining_name = ' '.join(scanning_state.remaining_name.split(' ')[1:])
            scanning_state.meta_data.language = self.salutations[first_word]["language"]
            scanning_state.meta_data.gender = self.salutations[first_word]["gender"]
            
            return scanning_state
        
        raise ValueError(f"Salutation '{first_word}' not found in dictionary.")
    


    def next_word_salutation(self, scanning_state: ScanningState) -> bool:
        
        first_word = scanning_state.remaining_name.split(' ')[0]

        if first_word in self.salutations:
            return True
        
        return False
        
        