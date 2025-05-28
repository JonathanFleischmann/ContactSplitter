import unittest
from persistency.letter_greeting_adder import LetterGreetingAdder
from generators.letter_greeting_generator import LetterGreetingGenerator
from data_structures.meta_data import Language, genders

class TestLetterGreetingAdder(unittest.TestCase):

    def setUp(self):
        # Reset genders to a known state
        genders.clear()
        genders.update({"Männlich", "Weiblich", "Divers", "Nichtbinär"})
        self.generator = LetterGreetingGenerator()
        # Remove test greeting if present
        self.generator.greetings.pop("Test Greeting", None)
        self.generator.include_name.pop("Test Greeting", None)
        self.adder = LetterGreetingAdder(self.generator)

    def test_add_new_greeting(self):
        self.adder.add_salutation("Test Greeting", Language.EN, "Männlich", True)
        self.assertIn("Test Greeting", self.generator.greetings)
        self.assertEqual(self.generator.greetings["Test Greeting"]["language"], Language.EN)
        self.assertEqual(self.generator.greetings["Test Greeting"]["gender"], "Männlich")
        self.assertTrue(self.generator.include_name["Test Greeting"])

    def test_add_greeting_unknown_gender_raises(self):
        with self.assertRaises(ValueError) as context:
            self.adder.add_salutation("Another Greeting", Language.EN, "UnknownGender", True)
        self.assertIn("Unknown gender", str(context.exception))

    def test_add_greeting_empty_string_raises(self):
        with self.assertRaises(ValueError) as context:
            self.adder.add_salutation("", Language.EN, "Männlich", True)
        self.assertIn("No empty string allowed", str(context.exception))

if __name__ == "__main__":
    unittest.main()
