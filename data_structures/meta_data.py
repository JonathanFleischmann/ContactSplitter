from dataclasses import dataclass
from enum import Enum

class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
    NON_BINARY = "non-binary"

class Language(Enum):
    EN = "Englisch"
    DE = "Deutsch"
    FR = "Französisch"
    ES = "Spanisch"
    IT = "Italienisch"
    PT = "Portugiesisch"
    PL = "Polnisch"
    CS = "Tschechisch"
    JA = "Japanisch"
    ZH = "Chinesisch"
    AR = "Arabisch"
    HI = "Hindi"
    VI = "Vietnamesisch"
    TH = "Thailändisch"
    RO = "Rumänisch"
    RU = "Russisch"
    SR = "Serbisch"
    BN = "Bengalisch"

@dataclass
class MetaData:
    gender: Gender | None
    language: str | None
    estimated_age: int | None

def convert_string_to_language(language: str) -> Language:
    try:
        return Language[language.upper()]
    except KeyError:
        raise ValueError(f"Invalid language: {language}")


