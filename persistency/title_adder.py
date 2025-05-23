from data_structures.meta_data import Language
from scanner.title_scanner import TitleScanner

class TitleAdder:

    title_scanner: TitleScanner

    def __init__(self, title_scanner: TitleScanner):
        self.title_scanner = title_scanner

    def add_title(self, title: str, language: Language) -> None:
        if title in self.title_scanner.titles:
            raise ValueError(f"Salutation '{title}' already exists in dictionary.")
        if title == "":
            raise ValueError(f"No empty string allowed.")
        
        self.title_scanner.titles[title] = language
        