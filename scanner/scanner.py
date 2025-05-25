from data_structures.scanning_state import ScanningState, MetaData
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner
import ai_integration  as ai_integration

class Scanner:

    salutation_scanner: SalutationScanner
    title_scanner: TitleScanner
    name_scanner: NameScanner


    def __init__(self, salutation_scanner: SalutationScanner, title_scanner: TitleScanner, name_scanner: NameScanner):
        self.salutation_scanner = salutation_scanner
        self.title_scanner = title_scanner
        self.name_scanner = name_scanner

    
    def scan_string(self, input_string: str) -> ScanningState:

        input_string = input_string.strip()
        
        if not input_string:
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
            gender = ai_integration.get_gender_for_name(scanner_state.get_first_name())
            scanner_state.meta_data.gender = gender
        
        age = ai_integration.get_age_for_name(scanner_state.get_name())
        scanner_state.meta_data.estimated_age = age

        return scanner_state.create_contact()