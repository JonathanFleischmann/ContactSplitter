import json
from data_structures.token import Token, TokenType
from data_structures.meta_data import Language
from data_structures.scanning_state import ScanningState
from core import get_longest_of_values_contained

class TitleScanner:
    """
    Scannt und erkennt Titel im Namen anhand eines Wörterbuchs.
    """

    file_path = 'dictionary_data/titles.json'

    def __init__(self):
        # Titel-Liste laden (alle als Deutsch)
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.titles: list[str] = json.load(file)

    def scan_title(self, scanning_state: ScanningState) -> ScanningState:
        """
        Sucht und entfernt den längsten passenden Titel aus dem Namen.
        """
        longest_found_title: str | None = get_longest_of_values_contained(
            scanning_state.remaining_name, self.titles)
        
        if longest_found_title is None:
            raise ValueError("Title not found in dictionary.")

        scanning_state.update(
            scanning_state.remaining_name.removeprefix(longest_found_title).strip(), 
            Token(TokenType.TITLE, longest_found_title), 
            Language.DE
        )

    def next_word_title(self, scanning_state: ScanningState) -> bool:
        """
        Prüft, ob das nächste Wort im Namen ein bekannter Titel ist.
        """
        return get_longest_of_values_contained(scanning_state.remaining_name, self.titles) is not None