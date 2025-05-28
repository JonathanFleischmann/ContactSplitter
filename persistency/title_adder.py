from data_structures.meta_data import Language
from scanner.title_scanner import TitleScanner

class TitleAdder:
    """
    Klasse zum Hinzufügen neuer Titel zum Titel-Wörterbuch.
    """

    def __init__(self, title_scanner: TitleScanner):
        self.title_scanner = title_scanner

    def add_title(self, title: str) -> None:
        """
        Fügt einen neuen Titel mit zugehöriger Sprache hinzu.
        Löst eine Exception aus, wenn der Titel leer ist oder bereits existiert.
        """
        if title in self.title_scanner.titles:
            raise ValueError("Title already exists in dictionary.")
        if title == "":
            raise ValueError("No empty string allowed.")
        self.title_scanner.titles.append(title)