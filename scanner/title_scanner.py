
import json
from data_structures.token import Token, TokenType
from data_structures.meta_data import Language, convert_string_to_language
from data_structures.scanning_state import ScanningState

class TitleScanner:

    file_path = 'dictionary_data/titles.json'

    def __init__(self):

        self.titles : dict[str, Language] = {}

        with open(self.file_path, 'r', encoding='utf-8') as file:
            loaded_titles = json.load(file)
            self.titles = {k: convert_string_to_language(v) for k, v in loaded_titles.items()}

    
    
    def scan_title(self, scanning_state: ScanningState) -> ScanningState:
        first_word = scanning_state.remaining_name.split(' ')[0]

        if first_word in self.titles:
            
            token = Token(TokenType.TITLE, first_word)

            scanning_state.token_list.append(token)
            scanning_state.remaining_name = ' '.join(scanning_state.remaining_name.split(' ')[1:])

            if scanning_state.meta_data.language == None:
                scanning_state.meta_data.language = self.titles[first_word]
            
            return scanning_state
        
        raise ValueError(f"Title '{first_word}' not found in title-dictionary.")
    


    def next_word_title(self, scanning_state: ScanningState) -> bool:
        
        first_word = scanning_state.remaining_name.split(' ')[0]

        if first_word in self.titles:
            return True
        
        return False
        
        