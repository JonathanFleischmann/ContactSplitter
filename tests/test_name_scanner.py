import unittest
from scanner.name_scanner import NameScanner
from data_structures.scanning_state import ScanningState
from data_structures.token import TokenType
from data_structures.meta_data import MetaData

def get_scanning_state(remaining_name):
    return ScanningState(
        remaining_name=remaining_name,
        token_list=[],
        meta_data=MetaData()
    )

class TestNameScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = NameScanner()

    def test_scan_name_valid(self):
        scanning_state = get_scanning_state("John Doe")
        self.scanner.scan_name(scanning_state)
        self.assertEqual(len(scanning_state.token_list), 1)
        self.assertEqual(scanning_state.token_list[0].type, TokenType.FIRST_NAME)
        self.assertEqual(scanning_state.token_list[0].value, "John")
        self.assertEqual(scanning_state.remaining_name, "Doe")

    def test_scan_name_empty(self):
        scanning_state = get_scanning_state(" ")
        with self.assertRaises(ValueError) as context:
            self.scanner.scan_name(scanning_state)
        self.assertIn("Invalid name", str(context.exception))

if __name__ == "__main__":
    unittest.main()
