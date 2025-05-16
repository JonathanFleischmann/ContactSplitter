# import ContactSplitter.ai_integration as ai_integration

# input = input("Enter a name: ")
# print(ai_integration.get_gender_for_name(input))
# print(ai_integration.get_age_for_name(input))

from scanner.scanner import Scanner

def main():
    input_string = input("Enter a name: ")
    scanner = Scanner()
    scanning_state = scanner.scan_string(input_string)
    
    print("Tokens:")
    for token in scanning_state.token_list:
        print(f"Type: {token.type}, Value: {token.value}")
    
    print(f"Remaining Name: {scanning_state.remaining_name}")
    print(f"Meta Data: {scanning_state.meta_data}")

if __name__ == "__main__":
    main()