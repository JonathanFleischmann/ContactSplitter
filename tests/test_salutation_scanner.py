import unittest
from scanner.salutation_scanner import SalutationScanner
from data_structures.scanning_state import ScanningState
from data_structures.meta_data import Language, MetaData

def get_scanning_state(remaining_name):
    return ScanningState(
        remaining_name=remaining_name,
        token_list=[],
        meta_data=MetaData()
    )

class TestSalutationScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = SalutationScanner()

    def test_scan_salutation_valid(self):
        scanning_state = get_scanning_state("Mr John Doe")
        self.scanner.scan_salutation(scanning_state)
        self.assertEqual(len(scanning_state.token_list), 0)
        self.assertEqual(scanning_state.remaining_name, "John Doe")
        self.assertEqual(scanning_state.meta_data.language, Language.EN)
        self.assertEqual(scanning_state.meta_data.gender, "Männlich")

    def test_scan_salutation_invalid(self):
        scanning_state = get_scanning_state("Dxr John Doe")
        with self.assertRaises(ValueError) as context:
            self.scanner.scan_salutation(scanning_state)
        self.assertIn("Salutation not found in dictionary", str(context.exception))

    def test_scan_salutation_multiple_salutations(self):
        scanning_state = get_scanning_state("Mr Mrs John Doe")
        with self.assertRaises(ValueError) as context:
            self.scanner.scan_salutation(scanning_state)
            self.scanner.scan_salutation(scanning_state)
        self.assertIn("Multiple salutations found", str(context.exception))


if __name__ == "__main__":
    unittest.main()