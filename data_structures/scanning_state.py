from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData
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