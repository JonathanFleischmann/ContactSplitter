from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    SALUTATION = "Anrede"
    TITLE = "Titel"
    FIRST_NAME = "Vorname"
    LAST_NAME = "Nachname"

@dataclass
class Token:
    type: TokenType
    value: str