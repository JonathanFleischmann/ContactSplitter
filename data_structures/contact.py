from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData
from dataclasses import dataclass
from data_structures.meta_data import Language

@dataclass
class Contact:
    token_list: list[Token]
    meta_data: MetaData

    def has_first_name(self) -> bool:
        """Prüft, ob ein Vorname vorhanden ist."""
        for token in self.token_list:
            if token.type == TokenType.FIRST_NAME:
                return True
        return False
    
    def has_last_name(self) -> bool:
        """Prüft, ob ein Nachname vorhanden ist."""
        for token in self.token_list:
            if token.type == TokenType.LAST_NAME:
                return True
        return False

    def has_salutation(self) -> bool:
        """Prüft, ob eine Anrede vorhanden ist."""
        for token in self.token_list:
            if token.type == TokenType.SALUTATION:
                return True
        return False

    def get_first_name(self) -> str:
        """Gibt alle Vornamen als String zurück."""
        first_names = [token.value for token in self.token_list if token.type == TokenType.FIRST_NAME]
        return " ".join(first_names).strip()

    def get_name(self) -> str:
        """
        Gibt den vollständigen Namen als String zurück.
        Mehrere Nachnamen werden mit Bindestrich verbunden.
        """
        if not self.token_list:
            return ""
        previous_token_type = self.token_list[0].type
        name = self.token_list[0].value

        for token in self.token_list[1:]:
            if token.type == TokenType.LAST_NAME and previous_token_type == TokenType.LAST_NAME:
                name += "-" + token.value
            else:
                name += " " + token.value
            previous_token_type = token.type
        return name.strip()
    
def get_empty_contact() -> Contact:
    """Erzeugt ein leeres Contact-Objekt mit Standardwerten."""
    meta_data = MetaData()
    meta_data.language = Language.DE
    meta_data.gender = "Nicht ermittelbar"
    meta_data.estimated_age = 0

    contact = Contact(
        token_list=[],
        meta_data=meta_data
    )
    return contact