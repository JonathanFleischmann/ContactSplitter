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
        
        for token in self.token_list:
            if token.type == TokenType.FIRST_NAME:
                return True
            
        return False
    
    def has_second_first_name(self) -> bool:
        first_names = 0
        
        for token in self.token_list:
            if token.type == TokenType.FIRST_NAME:
                first_names += 1
                if first_names > 1:
                    return True
        
        return False
    
    def create_contact(self) -> Contact:
        """
        Create a contact object this.
        """
        contact = Contact(self.token_list, self.meta_data)
        return contact
    
    def update(self, remaining_name: str, token: Token, language: Language = None, gender: str = None) -> None:
            
        self.remaining_name = remaining_name

        if gender is not None:
            self.meta_data.gender = gender

        if language is not None and (self.meta_data.language is None or token.type == TokenType.SALUTATION):
            self.meta_data.language = language

        if token.type == TokenType.SALUTATION:
            if self.salutation_found:
                raise ValueError(f"Multiple salutations found")
            self.salutation_found = True
            return
        
        self.token_list.append(token)

    def get_first_name(self) -> str:
        first_names = []
        
        for token in self.token_list:
            if token.type == TokenType.FIRST_NAME:
                first_names.append(token.value)
        
        return " ".join(first_names).strip()
    

    def get_name(self) -> str:
        name = ""

        for token in self.token_list:
            name += token.value + " "
            
        return name.strip()