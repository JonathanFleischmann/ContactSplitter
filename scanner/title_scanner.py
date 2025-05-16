
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
        
        remaining_name = scanning_state.remaining_name

        longest_found_title: str | None = None

        for title in self.titles:
            
            if remaining_name.startswith(title):
                if longest_found_title is None or len(title) > len(longest_found_title):
                    longest_found_title = title
                

        if longest_found_title is not None:
            
            token = Token(TokenType.TITLE, longest_found_title)

            scanning_state.token_list.append(token)
            scanning_state.remaining_name = remaining_name.removeprefix(longest_found_title).strip()

            if scanning_state.meta_data.language == None:
                scanning_state.meta_data.language = self.titles[longest_found_title]
            
            return scanning_state
        
        raise ValueError(f"No title found in {remaining_name}.")
    


    def next_word_title(self, scanning_state: ScanningState) -> bool:
        
        remaining_name = scanning_state.remaining_name

        longest_found_title: str | None = None

        for title in self.titles:
            
            if remaining_name.startswith(title):
                if longest_found_title is None or len(title) > len(longest_found_title):
                    return True
                
        return False
        
        