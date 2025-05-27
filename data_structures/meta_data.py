from dataclasses import dataclass
from enum import Enum



genders = {
    "Männlich",
    "Weiblich",
    "Nichtbinär",
    "Divers",
    "Agender",
    "Genderfluid",
    "Nicht ermittelbar"
}


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
    gender: str | None
    language: Language | None

    def __init__(self):
        self.gender = None
        self.language = None



def convert_string_to_language(language: str) -> Language:
    if isinstance(language, Language):
        return language
    try:
        return Language[language.upper()]
    except KeyError:
        raise ValueError(f"Invalid language: {language}")



