from data_structures.scanning_state import ScanningState, MetaData
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner

class Scanner:
    
    def scan_string(self, input_string: str) -> str:

        input_string = input_string.strip()
        
        if not input_string:
            raise ValueError("Input string is empty")
        
        empty_meta_data = MetaData()
        scanner_state = ScanningState(token_list=[], meta_data=empty_meta_data, remaining_name=input_string)

        salutation_scanner = SalutationScanner()
        title_scanner = TitleScanner()
        name_scanner = NameScanner()

        while scanner_state.remaining_name.strip() != '':
            # Scan for title
            if salutation_scanner.next_word_salutation(scanner_state):
                salutation_scanner.scan_salutation(scanner_state)
            elif title_scanner.next_word_title(scanner_state):
                title_scanner.scan_title(scanner_state)
            else:
                name_scanner.scan_name(scanner_state)

        return scanner_state