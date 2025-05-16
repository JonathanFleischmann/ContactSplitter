
import json
from data_structures.token import Token, TokenType
from data_structures.meta_data import Language, convert_string_to_language
from data_structures.scanning_state import ScanningState

class NameScanner:
        
    file_path = 'dictionary_data/nobility_particles.json'

    def __init__(self):

        self.nobility_particles : dict[str, Language] = {}

        with open(self.file_path, 'r', encoding='utf-8') as file:
            loaded_nobility_particles = json.load(file)
            self.nobility_particles = {k: convert_string_to_language(v) for k, v in loaded_nobility_particles.items()}



    def scan_name(self, scanning_state: ScanningState) -> ScanningState:

        remaining_name = scanning_state.remaining_name

        longest_found_nobility_particle: str | None = None

        for nobility_particle in self.nobility_particles:
            
            if remaining_name.startswith(nobility_particle):
                if longest_found_nobility_particle is None or len(nobility_particle) > len(longest_found_nobility_particle):
                    longest_found_nobility_particle = nobility_particle
                

        if longest_found_nobility_particle is not None:

            if remaining_name.removeprefix(longest_found_nobility_particle).strip() == '':
                raise ValueError(f"Name '{remaining_name}' is empty after removing nobility particle '{longest_found_nobility_particle}'")
            
            name_after_nobility_particle = remaining_name.removeprefix(longest_found_nobility_particle).strip().split(' ')[0]

            if name_after_nobility_particle[0].islower():
                raise ValueError(f"Unknown name construction '{remaining_name}'")
            
            scanning_state.remaining_name = ' '.join(name_after_nobility_particle.split(' ')[1:])

            token = Token(TokenType.LAST_NAME, longest_found_nobility_particle + " " + name_after_nobility_particle)
            scanning_state.token_list.append(token)

            if scanning_state.meta_data.language == None:
                scanning_state.meta_data.language = self.nobility_particles[longest_found_nobility_particle]

            return scanning_state
        
        else:

            if remaining_name.split(' ')[0].islower():
                raise ValueError(f"Unknown name construction '{remaining_name}'")
            
            if scanning_state.has_first_name():
                
                last_name = remaining_name.split(' ')[0]

                scanning_state.remaining_name = ' '.join(scanning_state.remaining_name.split(' ')[1:])
                token = Token(TokenType.LAST_NAME, last_name)
                scanning_state.token_list.append(token)
                return scanning_state
            
            else:

                if len(remaining_name.split(' ')) == 1:

                    last_name = remaining_name.split(' ')[0]

                    scanning_state.remaining_name = ' '.join(scanning_state.remaining_name.split(' ')[1:])
                    token = Token(TokenType.LAST_NAME, last_name)
                    scanning_state.token_list.append(token)
                    return scanning_state
                
                else:

                    first_name = remaining_name.split(' ')[0]

                    scanning_state.remaining_name = ' '.join(remaining_name.split(' ')[1:])
                    token = Token(TokenType.FIRST_NAME, first_name)
                    scanning_state.token_list.append(token)
                    return scanning_state
                    


            
 