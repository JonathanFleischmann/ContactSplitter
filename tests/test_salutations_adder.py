import unittest
from persistency.salutations_adder import SalutationAdder
from scanner.salutation_scanner import SalutationScanner
from data_structures.meta_data import Language, genders

class TestSalutationAdder(unittest.TestCase):

    def setUp(self):
        # Reset genders and salutations before each test
        genders.clear()
        genders.update({"Männlich", "Weiblich"})
        self.scanner = SalutationScanner()
        self.scanner.salutations.clear()
        self.adder = SalutationAdder(self.scanner)

    def test_add_new_salutation(self):
        self.adder.add_salutation("Mrr", Language.EN, "Männlich")
        self.assertIn("Mrr", self.scanner.salutations)
        self.assertEqual(self.scanner.salutations["Mrr"]["language"], Language.EN)
        self.assertEqual(self.scanner.salutations["Mrr"]["gender"], "Männlich")

    def test_add_existing_salutation_raises(self):
        self.scanner.salutations["Mr"] = {"language": Language.EN, "gender": "Männlich"}
        with self.assertRaises(ValueError) as context:
            self.adder.add_salutation("Mr", Language.EN, "Männlich")
        self.assertIn("already exists", str(context.exception))

    def test_add_salutation_unknown_gender_raises(self):
        with self.assertRaises(ValueError) as context:
            self.adder.add_salutation("Mx", Language.EN, "Divers")
        self.assertIn("Unknown gender", str(context.exception))

if __name__ == "__main__":
    unittest.main()
