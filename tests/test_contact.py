import unittest
from data_structures.contact import Contact, get_empty_contact
from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData, Language

class TestContact(unittest.TestCase):

    def setUp(self):
        self.tokens = [
            Token(TokenType.SALUTATION, "Mr"),
            Token(TokenType.FIRST_NAME, "John"),
            Token(TokenType.LAST_NAME, "Doe")
        ]
        self.meta_data = MetaData()
        self.contact = Contact(token_list=self.tokens, meta_data=self.meta_data)

    def test_has_first_name_true(self):
        self.assertTrue(self.contact.has_first_name())

    def test_has_first_name_false(self):
        contact = Contact(token_list=[Token(TokenType.LAST_NAME, "Doe")], meta_data=self.meta_data)
        self.assertFalse(contact.has_first_name())

    def test_has_salutation_true(self):
        self.assertTrue(self.contact.has_salutation())

    def test_has_salutation_false(self):
        contact = Contact(token_list=[Token(TokenType.FIRST_NAME, "John")], meta_data=self.meta_data)
        self.assertFalse(contact.has_salutation())

    def test_get_first_name(self):
        self.assertEqual(self.contact.get_first_name(), "John")

    def test_get_first_name_multiple(self):
        tokens = [
            Token(TokenType.FIRST_NAME, "John"),
            Token(TokenType.FIRST_NAME, "Michael"),
            Token(TokenType.LAST_NAME, "Doe")
        ]
        contact = Contact(token_list=tokens, meta_data=self.meta_data)
        self.assertEqual(contact.get_first_name(), "John Michael")

    def test_get_first_name_none(self):
        contact = Contact(token_list=[Token(TokenType.LAST_NAME, "Doe")], meta_data=self.meta_data)
        self.assertEqual(contact.get_first_name(), "")

    def test_get_name(self):
        self.assertEqual(self.contact.get_name(), "Mr John Doe")

    def test_get_empty_contact(self):
        empty_contact = get_empty_contact()
        self.assertEqual(empty_contact.token_list, [])
        self.assertEqual(empty_contact.meta_data.language, Language.DE)
        self.assertEqual(empty_contact.meta_data.gender, "Nicht ermittelbar")
        self.assertEqual(empty_contact.meta_data.estimated_age, 0)

if __name__ == "__main__":
    unittest.main()
