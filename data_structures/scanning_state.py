from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData, Language
from data_structures.contact import Contact
from dataclasses import dataclass

@dataclass
class ScanningState:
    token_list: list[Token]
    meta_data: MetaData
    remaining_name: str
    salutation_found: bool = False

    def has_first_name(self) -> bool:
        """Prüft, ob ein Vorname im Token-List vorhanden ist."""
        for token in self.token_list:
            if token.type == TokenType.FIRST_NAME:
                return True
        return False
    
    def has_second_first_name(self) -> bool:
        """Prüft, ob mehr als ein Vorname vorhanden ist."""
        first_names = 0
        for token in self.token_list:
            if token.type == TokenType.FIRST_NAME:
                first_names += 1
                if first_names > 1:
                    return True
        return False
    
    def create_contact(self) -> Contact:
        """Erstellt ein Contact-Objekt aus dem aktuellen Zustand."""
        return Contact(self.token_list, self.meta_data)
    
    def update(self, remaining_name: str, token: Token, language: Language = None, gender: str = None) -> None:
        """
        Aktualisiert den ScanningState mit neuem Token, Sprache und ggf. Gender.
        """
        self.remaining_name = remaining_name

        if gender is not None:
            self.meta_data.gender = gender

        if language is not None and (self.meta_data.language is None or token.type == TokenType.SALUTATION):
            self.meta_data.language = language

        if token.type == TokenType.SALUTATION:
            if self.salutation_found:
                raise ValueError("Multiple salutations found")
            self.salutation_found = True
            return
        
        self.token_list.append(token)

    def get_first_name(self) -> str:
        """Gibt alle Vornamen als String zurück."""
        first_names = [token.value for token in self.token_list if token.type == TokenType.FIRST_NAME]
        return " ".join(first_names).strip()
    
    def get_name(self) -> str:
        """Gibt den vollständigen Namen als String zurück."""
        return " ".join(token.value for token in self.token_list).strip()