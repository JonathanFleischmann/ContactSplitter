from data_structures.scanning_state import ScanningState, MetaData
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner
from data_structures.meta_data import Language
from data_structures.contact import Contact
import scanner.ai_integration  as ai_integration
from core import flip_names_on_comma_between

class Scanner:

    salutation_scanner: SalutationScanner
    title_scanner: TitleScanner
    name_scanner: NameScanner


    def __init__(self, salutation_scanner: SalutationScanner, title_scanner: TitleScanner, name_scanner: NameScanner):
        self.salutation_scanner = salutation_scanner
        self.title_scanner = title_scanner
        self.name_scanner = name_scanner

    
    def scan_string(self, input_string: str) -> Contact:

        # Flip names on comma if necessary
        input_string = flip_names_on_comma_between(input_string)
        
        if not input_string or input_string.strip() == '':
            raise ValueError("Input string is empty")
        
        empty_meta_data = MetaData()
        scanner_state = ScanningState(token_list=[], meta_data=empty_meta_data, remaining_name=input_string)


        while scanner_state.remaining_name.strip() != '':
            # Scan for title
            if self.salutation_scanner.next_word_salutation(scanner_state):
                self.salutation_scanner.scan_salutation(scanner_state)
            elif self.title_scanner.next_word_title(scanner_state):
                self.title_scanner.scan_title(scanner_state)
            else:
                self.name_scanner.scan_name(scanner_state)

        if scanner_state.meta_data.gender == None or scanner_state.meta_data.gender == "":
            if scanner_state.has_first_name():
                gender = ai_integration.get_gender_for_name(scanner_state.get_first_name())
            else:
                gender = "Nicht ermittelbar"
            scanner_state.meta_data.gender = gender
        

        contact = scanner_state.create_contact()
        if contact.meta_data.language is None:
            contact.meta_data.language = Language.DE

        return contact