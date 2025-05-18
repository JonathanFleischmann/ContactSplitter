import unittest
from scanner.title_scanner import TitleScanner
from data_structures.scanning_state import ScanningState
from data_structures.token import TokenType
from data_structures.meta_data import MetaData

def get_scanning_state(remaining_name):
    return ScanningState(
        remaining_name=remaining_name,
        token_list=[],
        meta_data=MetaData()
    )

class TestTitleScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = TitleScanner()

    def test_scan_title_valid(self):
        scanning_state = get_scanning_state("Dr. John Doe")
        self.scanner.scan_title(scanning_state)
        self.assertEqual(len(scanning_state.token_list), 1)
        self.assertEqual(scanning_state.token_list[0].type, TokenType.TITLE)
        self.assertEqual(scanning_state.token_list[0].value, "Dr.")
        self.assertEqual(scanning_state.remaining_name, "John Doe")

    def test_scan_title_invalid(self):
        scanning_state = get_scanning_state("Xyz John Doe")
        with self.assertRaises(ValueError) as context:
            self.scanner.scan_title(scanning_state)
        self.assertIn("Title not found", str(context.exception))

    def test_next_word_title_true(self):
        scanning_state = get_scanning_state("Dr. John Doe")
        self.assertTrue(self.scanner.next_word_title(scanning_state))

    def test_next_word_title_false(self):
        scanning_state = get_scanning_state("Xyz John Doe")
        self.assertFalse(self.scanner.next_word_title(scanning_state))

if __name__ == "__main__":
    unittest.main()
