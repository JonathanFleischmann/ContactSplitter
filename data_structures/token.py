from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    SALUTATION = "salutation"
    TITLE = "title"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"

@dataclass
class Token:
    type: TokenType
    value: str