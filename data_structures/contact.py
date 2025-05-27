from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData
from dataclasses import dataclass
from data_structures.meta_data import Language

@dataclass
class Contact:
    token_list: list[Token]
    meta_data: MetaData


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
    
def get_empty_contact() -> Contact:
        meta_data = MetaData()
        meta_data.language = Language.DE
        meta_data.gender = "Nicht ermittelbar"
        meta_data.estimated_age = 0

        contact = Contact(
            token_list=[],
            meta_data=meta_data
        )
        return contact