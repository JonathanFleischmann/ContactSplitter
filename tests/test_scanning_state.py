import unittest
from data_structures.scanning_state import ScanningState
from data_structures.token import Token, TokenType
from data_structures.meta_data import MetaData, Language

class TestScanningState(unittest.TestCase):

    def setUp(self):
        self.meta_data = MetaData()
        self.state = ScanningState(token_list=[], meta_data=self.meta_data, remaining_name="John Doe")

    def test_has_first_name_true(self):
        self.state.token_list.append(Token(TokenType.FIRST_NAME, "John"))
        self.assertTrue(self.state.has_first_name())

    def test_has_first_name_false(self):
        self.state.token_list.append(Token(TokenType.LAST_NAME, "Doe"))
        self.assertFalse(self.state.has_first_name())

    def test_update_adds_token_and_updates_remaining_name(self):
        self.state.update("Doe", Token(TokenType.FIRST_NAME, "John"), Language.EN)
        self.assertEqual(len(self.state.token_list), 1)
        self.assertEqual(self.state.token_list[0].value, "John")
        self.assertEqual(self.state.remaining_name, "Doe")
        self.assertEqual(self.state.meta_data.language, Language.EN)

    def test_update_sets_gender(self):
        self.state.update("Doe", Token(TokenType.FIRST_NAME, "John"), gender="Männlich")
        self.assertEqual(self.state.meta_data.gender, "Männlich")


    def test_get_first_name(self):
        self.state.token_list.append(Token(TokenType.FIRST_NAME, "John"))
        self.state.token_list.append(Token(TokenType.FIRST_NAME, "Michael"))
        self.assertEqual(self.state.get_first_name(), "John Michael")

    def test_get_first_name_empty(self):
        self.assertEqual(self.state.get_first_name(), "")

    def test_get_name(self):
        self.state.token_list.append(Token(TokenType.SALUTATION, "Mr"))
        self.state.token_list.append(Token(TokenType.FIRST_NAME, "John"))
        self.state.token_list.append(Token(TokenType.LAST_NAME, "Doe"))
        self.assertEqual(self.state.get_name(), "Mr John Doe")

    def test_create_contact(self):
        self.state.token_list.append(Token(TokenType.FIRST_NAME, "John"))
        contact = self.state.create_contact()
        self.assertEqual(contact.token_list[0].value, "John")
        self.assertIs(contact.meta_data, self.state.meta_data)

if __name__ == "__main__":
    unittest.main()
