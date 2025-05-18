from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData, Language
from data_structures.contact import Contact
from dataclasses import dataclass

@dataclass
class ScanningState:
    token_list: list[Token]
    meta_data: MetaData
    remaining_name: str

    def has_first_name(self) -> bool:
        
        for token in self.token_list:
            if token.type == TokenType.FIRST_NAME:
                return True
            
        return False
    
    def has_salutation(self) -> bool:
        
        for token in self.token_list:
            if token.type == TokenType.SALUTATION:
                return True
            
        return False
    
    def create_contact(self) -> str:
        """
        Create a contact object this.
        """
        contact = Contact(self.token_list, self.meta_data)
        return contact
    
    def update(self, token: Token, remaining_name: str, language: Language = None, gender: str = None) -> None:

        if token.type == TokenType.SALUTATION and self.has_salutation():
            raise ValueError(f"Multiple salutations found")

        self.token_list.append(token)
        self.remaining_name = remaining_name
        if gender is not None:
            self.meta_data.gender = gender

        if language is not None and (self.meta_data.language is None or token.type == TokenType.SALUTATION):
            self.meta_data.language = language