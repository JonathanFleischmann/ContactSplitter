import ai_integration as ai_integration
from data_structures.scanning_state import MetaData, Language, Contact
from scanner.scanner import Scanner
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner
from generators.letter_greeting_generator import LetterGreetingGenerator
from data_structures.contact import Contact
from persistency.contact_saver import ContactSaver
from user_interface.user_interface import UserInterface

def main():
    salutation_scanner = SalutationScanner()
    title_scanner = TitleScanner()
    name_scanner = NameScanner()
    scanner = Scanner(salutation_scanner, title_scanner, name_scanner)

    contact_saver = ContactSaver()

    meta_data = MetaData()
    meta_data.language = Language.DE
    meta_data.gender = "Divers"
    meta_data.estimated_age = 0

    contact = Contact(
        token_list=[],
        meta_data=meta_data
    )

    UserInterface().start_ui(scanner, contact_saver, contact)



    

if __name__ == "__main__":
    main()