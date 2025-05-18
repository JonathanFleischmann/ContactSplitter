
import json
from data_structures.token import Token, TokenType
from data_structures.meta_data import Language, convert_string_to_language
from data_structures.scanning_state import ScanningState
from core import get_longest_of_values_contained, pop_first_word

class NameScanner:
        
    file_path = 'dictionary_data/nobility_particles.json'

    def __init__(self):

        self.nobility_particles : dict[str, Language] = {}

        with open(self.file_path, 'r', encoding='utf-8') as file:
            loaded_nobility_particles = json.load(file)
            self.nobility_particles = {k: convert_string_to_language(v) for k, v in loaded_nobility_particles.items()}
                    


    def is_valid_name_after_prefix(self, remaining_name: str, prefix: str) -> bool:
        name = remaining_name.removeprefix(prefix).strip()
        if name == "":
            raise ValueError(f"Invalid name: No name after prefix '{prefix}' found in '{remaining_name}'.")
        if not name.split(' ')[0][0].isupper():
            raise ValueError(f"Invalid name: Name after prefix '{prefix}' isn't a capitalized character: '{name}.'")
        return True



    def scan_name(self, scanning_state: ScanningState) -> ScanningState:
        
        nobility_particle: str = get_longest_of_values_contained(
            scanning_state.remaining_name, self.nobility_particles.keys()
        ) or ""
        
        if not self.is_valid_name_after_prefix(scanning_state.remaining_name, nobility_particle):
            return scanning_state
        
        name_part, rest = pop_first_word(scanning_state.remaining_name.removeprefix(nobility_particle).strip())
        last_name = f"{nobility_particle} {name_part}".strip() if nobility_particle else name_part

        token_type = TokenType.LAST_NAME if scanning_state.has_first_name() or len(scanning_state.remaining_name.split(' ')) == 1 else TokenType.FIRST_NAME
        
        language: Language | None = self.nobility_particles.get(nobility_particle)

        scanning_state.update(
            Token(token_type, last_name),
            rest,
            language
        )