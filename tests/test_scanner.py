import unittest
from scanner.scanner import Scanner
from scanner.salutation_scanner import SalutationScanner
from scanner.title_scanner import TitleScanner
from scanner.name_scanner import NameScanner
from data_structures.token import TokenType
from data_structures.meta_data import Language

def get_scanner():
    return Scanner(
        SalutationScanner(),
        TitleScanner(),
        NameScanner()
    )

class TestScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = get_scanner()

    def test_scan_string_salutation_title_name(self):
        result = self.scanner.scan_string("Mx Dr. John Doe")
        self.assertEqual(len(result.token_list), 4)
        self.assertEqual(result.token_list[0].type, TokenType.SALUTATION)
        self.assertEqual(result.token_list[0].value, "Mx")
        self.assertEqual(result.token_list[1].type, TokenType.TITLE)
        self.assertEqual(result.token_list[1].value, "Dr.")
        self.assertEqual(result.token_list[2].type, TokenType.FIRST_NAME)
        self.assertEqual(result.token_list[2].value, "John")
        self.assertEqual(result.token_list[3].type, TokenType.LAST_NAME)
        self.assertEqual(result.token_list[3].value, "Doe")
        self.assertEqual(result.meta_data.language, Language.EN)
        self.assertEqual(result.meta_data.gender, "Nichtbinär")

    def test_scan_string_title_name(self):
        result = self.scanner.scan_string("Dr. John Doe")
        self.assertEqual(len(result.token_list), 3)
        self.assertEqual(result.token_list[0].type, TokenType.TITLE)
        self.assertEqual(result.token_list[0].value, "Dr.")
        self.assertEqual(result.token_list[1].type, TokenType.FIRST_NAME)
        self.assertEqual(result.token_list[1].value, "John")
        self.assertEqual(result.token_list[2].type, TokenType.LAST_NAME)
        self.assertEqual(result.token_list[2].value, "Doe")

    def test_scan_string_name_only(self):
        result = self.scanner.scan_string("John Doe")
        self.assertEqual(len(result.token_list), 2)
        self.assertEqual(result.token_list[0].type, TokenType.FIRST_NAME)
        self.assertEqual(result.token_list[0].value, "John")
        self.assertEqual(result.token_list[1].type, TokenType.LAST_NAME)
        self.assertEqual(result.token_list[1].value, "Doe")

    def test_scan_string_empty(self):
        with self.assertRaises(ValueError) as context:
            self.scanner.scan_string(" ")
        self.assertIn("Input string is empty", str(context.exception))

    def test_scan_string_invalid(self):
        with self.assertRaises(ValueError):
            self.scanner.scan_string("123")

if __name__ == "__main__":
    unittest.main()
