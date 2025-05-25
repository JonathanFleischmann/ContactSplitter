import ai_integration as ai_integration

# input = input("Enter a name: ")
# print(ai_integration.get_gender_for_name(input))
# print(ai_integration.get_age_for_name(input))

from scanner.scanner import Scanner
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner
from persistency.salutations_adder import SalutationAdder
from persistency.gender_adder import GenderAdder
from persistency.title_adder import TitleAdder
from generators.letter_greeting_generator import LetterGreetingGenerator
from data_structures.contact import Contact

def main():
    salutation_scanner = SalutationScanner()
    title_scanner = TitleScanner()
    name_scanner = NameScanner()
    scanner = Scanner(salutation_scanner, title_scanner, name_scanner)

    salutation_adder = SalutationAdder(salutation_scanner)
    title_adder = TitleAdder(title_scanner)
    gender_adder = GenderAdder()

    letter_greeting_generator = LetterGreetingGenerator()

    input_string = input("Enter a name: ")
    contact : Contact = scanner.scan_string(input_string)

    # KI-Integration: Geschlecht und Alter ermitteln
    if contact.meta_data.gender is None:
        gender = ai_integration.get_gender_for_name(contact.get_first_name())
        contact.meta_data.gender = gender
        
    age = ai_integration.get_age_for_name(contact.get_name())
    contact.meta_data.estimated_age = age


    print("Tokens:")
    for token in contact.token_list:
        print(f"Type: {token.type}, Value: {token.value}")
    
    print(f"Meta Data: {contact.meta_data}")

    print(letter_greeting_generator.generate(contact))

if __name__ == "__main__":
    main()