import unittest
from persistency.gender_adder import GenderAdder
from data_structures.meta_data import genders

class TestGenderAdder(unittest.TestCase):

    def setUp(self):
        # Reset genders set before each test
        genders.clear()
        genders.update({"Männlich", "Weiblich"})
        self.gender_adder = GenderAdder()

    def test_add_new_gender(self):
        self.gender_adder.add_gender("Divers")
        self.assertIn("Divers", genders)

    def test_add_existing_gender_raises(self):
        with self.assertRaises(ValueError) as context:
            self.gender_adder.add_gender("Männlich")
        self.assertIn("already known", str(context.exception))

if __name__ == "__main__":
    unittest.main()
