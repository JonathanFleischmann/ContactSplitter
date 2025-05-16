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
    RO = "Rumänisch"
    SR = "Serbisch"



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


def convert_string_to_gender(gender: str) -> Gender:
    match gender.lower():
        case "w":
            return Gender.FEMALE
        case "m":
            return Gender.MALE
        case "nb":
            return Gender.NON_BINARY
        case _:
            raise ValueError(f"Invalid gender: {gender}")


