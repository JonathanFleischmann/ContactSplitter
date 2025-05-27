import unittest
from generators.letter_greeting_generator import LetterGreetingGenerator
from data_structures.contact import Contact
from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData, Language

class TestLetterGreetingGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = LetterGreetingGenerator()

    def make_contact(self, gender="Männlich", lang=Language.DE, tokens=None):
        meta = MetaData()
        meta.gender = gender
        meta.language = lang
        if tokens is None:
            tokens = [
                Token(TokenType.TITLE, "Dr"),
                Token(TokenType.LAST_NAME, "Mustermann")
            ]
        return Contact(token_list=tokens, meta_data=meta)

    def test_generate_greeting_with_name(self):
        contact = self.make_contact(gender="Männlich", lang=Language.DE)
        greeting = self.generator.generate(contact)
        self.assertIn("Sehr geehrter Herr", greeting)
        self.assertIn("Dr", greeting)
        self.assertIn("Mustermann", greeting)
        self.assertTrue(greeting.endswith(","))

    def test_generate_greeting_without_name(self):
        contact = self.make_contact(gender="", lang=Language.EN, tokens=[])
        greeting = self.generator.generate(contact)
        self.assertIn("Dear", greeting)
        self.assertTrue(greeting.endswith(","))

    def test_generate_greeting_fallback(self):
        contact = self.make_contact(gender="Divers", lang=Language.DE, tokens=[])
        greeting = self.generator.generate(contact)
        self.assertIn("Hallo", greeting)
        self.assertTrue(greeting.endswith(","))

    def test_get_greeting_exact_match(self):
        contact = self.make_contact(gender="Weiblich", lang=Language.DE)
        greeting, include_name = self.generator.get_greeting(contact, Language.DE)
        self.assertEqual(greeting, "Sehr geehrte Frau")
        self.assertTrue(include_name)

    def test_get_greeting_gender_neutral(self):
        contact = self.make_contact(gender="", lang=Language.FR)
        greeting, include_name = self.generator.get_greeting(contact, Language.FR)
        self.assertEqual(greeting, "Messieursdames")
        self.assertTrue(include_name)

if __name__ == "__main__":
    unittest.main()
