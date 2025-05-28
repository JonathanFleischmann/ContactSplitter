import json
from data_structures.token import Token, TokenType
from data_structures.meta_data import Language, convert_string_to_language
from data_structures.scanning_state import ScanningState
from core import get_longest_of_values_contained, pop_first_word

class NameScanner:
    """
    Scannt Namensteile und erkennt Adelsprädikate im Namen.
    """

    file_path = 'dictionary_data/nobility_particles.json'

    def __init__(self):
        # Adelsprädikate laden (z.B. "von", "zu", ...)
        self.nobility_particles: dict[str, Language] = {}
        with open(self.file_path, 'r', encoding='utf-8') as file:
            loaded_nobility_particles = json.load(file)
            self.nobility_particles = {k: convert_string_to_language(v) for k, v in loaded_nobility_particles.items()}

    def is_valid_name_after_prefix(self, remaining_name: str, prefix: str) -> bool:
        """
        Prüft, ob nach einem Adelsprädikat noch ein Name folgt.
        """
        name = remaining_name.removeprefix(prefix).strip()
        if name == "":
            if prefix != "":
                raise ValueError("Invalid name: No name after prefix.")
            else:
                raise ValueError("Invalid name.")
        return True

    def scan_name(self, scanning_state: ScanningState) -> ScanningState:
        """
        Erkennt und verarbeitet einen Namensteil (Vorname, Nachname, ggf. mit Adelsprädikat).
        """
        nobility_particle: str = get_longest_of_values_contained(
            scanning_state.remaining_name, self.nobility_particles.keys()
        ) or ""
        
        if not self.is_valid_name_after_prefix(scanning_state.remaining_name, nobility_particle):
            return scanning_state
        
        name_part, rest = pop_first_word(scanning_state.remaining_name.removeprefix(nobility_particle).strip())
        name = f"{nobility_particle} {name_part}".strip() if nobility_particle else name_part

        # Bestimme Token-Typ (Vorname oder Nachname)
        if nobility_particle:
            token_type = TokenType.LAST_NAME
        elif (not scanning_state.has_first_name or not scanning_state.has_second_first_name()) and len(rest.split(' ')) > 0 and rest.split(' ') != ['']:
            token_type = TokenType.FIRST_NAME
        else:
            token_type = TokenType.LAST_NAME
        
        language: Language | None = self.nobility_particles.get(nobility_particle)

        scanning_state.update(
            rest,
            Token(token_type, name),
            language
        )