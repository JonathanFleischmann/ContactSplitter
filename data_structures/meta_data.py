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
    gender: Gender
    language: str
    estimated_age: int


