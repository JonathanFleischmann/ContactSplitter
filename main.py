import scanner.ai_integration as ai_integration
from data_structures.scanning_state import MetaData, Language, Contact
from scanner.scanner import Scanner
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner
from persistency.contact_saver import ContactSaver
from user_interface.user_interface import UserInterface

def main():
    salutation_scanner = SalutationScanner()
    title_scanner = TitleScanner()
    name_scanner = NameScanner()
    scanner = Scanner(salutation_scanner, title_scanner, name_scanner)

    contact_saver = ContactSaver()

    UserInterface().start_ui(scanner, contact_saver, scanner.get_empty_contact())

    

if __name__ == "__main__":
    main()