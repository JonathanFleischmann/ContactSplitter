import unittest
from persistency.title_adder import TitleAdder
from scanner.title_scanner import TitleScanner
from data_structures.meta_data import Language

class TestTitleAdder(unittest.TestCase):

    def setUp(self):
        self.scanner = TitleScanner()
        self.scanner.titles.clear()
        self.adder = TitleAdder(self.scanner)

    def test_add_new_title(self):
        self.adder.add_title("Proff")
        self.assertIn("Proff", self.scanner.titles)

    def test_add_existing_title_raises(self):
        self.scanner.titles = ["Dr.", "Prof."]
        with self.assertRaises(ValueError) as context:
            self.adder.add_title("Dr.")
        self.assertIn("already exists", str(context.exception))

if __name__ == "__main__":
    unittest.main()
