# import ai_integration as ai_integration

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

def main():
    salutation_scanner = SalutationScanner()
    title_scanner = TitleScanner()
    name_scanner = NameScanner()
    scanner = Scanner(salutation_scanner, title_scanner, name_scanner)

    salutation_adder = SalutationAdder(salutation_scanner)
    title_adder = TitleAdder(title_scanner)
    gender_adder = GenderAdder()

    input_string = input("Enter a name: ")
    scanning_state = scanner.scan_string(input_string)
    
    print("Tokens:")
    for token in scanning_state.token_list:
        print(f"Type: {token.type}, Value: {token.value}")
    
    print(f"Remaining Name: {scanning_state.remaining_name}")
    print(f"Meta Data: {scanning_state.meta_data}")

if __name__ == "__main__":
    main()