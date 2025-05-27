from scanner.scanner import Scanner
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner
from user_interface.user_interface import UserInterface
from data_store.contact_list import ContactList

def main():
    salutation_scanner = SalutationScanner()
    title_scanner = TitleScanner()
    name_scanner = NameScanner()
    scanner = Scanner(salutation_scanner, title_scanner, name_scanner)

    contact_list = ContactList()

    UserInterface().start_ui(scanner, contact_list)

    

if __name__ == "__main__":
    main()