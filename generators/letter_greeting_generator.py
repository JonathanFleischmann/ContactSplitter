import json
import os

from data_structures.contact import Contact
from data_structures.meta_data import Language, convert_string_to_language
from data_structures.token import Token, TokenType

class LetterGreetingGenerator:

    file_path = 'dictionary_data/letter_greeting.json'

    def __init__(self):

        self.greetings : dict[str, dict[Language, str]] = {}
        self.include_name  = {}

        with open(self.file_path, 'r', encoding='utf-8') as file:
            loaded_greetings = json.load(file)
            self.greetings = {
                key: {
                    "lang": convert_string_to_language(value["lang"]),
                    "gender": value["gender"],
                }
                for key, value in loaded_greetings.items()
            }
            self.include_name = {
                key: value.get("include_name", False)
                for key, value in loaded_greetings.items()
            }

    def generate(self, contact: Contact, lang: Language = None) -> str:
        if lang is None:
            lang = contact.meta_data.language
        greeting, include_name = self.get_greeting(contact, lang, contact.has_last_name())
        if not include_name:
            return greeting + ","
        for token in contact.token_list:
            if token.type == TokenType.TITLE:
                greeting = greeting + " " + token.value
        multiple_last_names = False
        for token in contact.token_list:
            if token.type == TokenType.LAST_NAME:
                if multiple_last_names:
                    greeting = greeting + "-" + token.value
                else:
                    greeting = greeting + " " + token.value
                    multiple_last_names = True
        greeting = greeting + ","
        return greeting 


    
    def get_greeting(self, contact: Contact, lang: Language, name_available: bool) -> str:
        gender = contact.meta_data.gender
            

        for greeting, data in self.greetings.items():
            if convert_string_to_language(data["lang"]) == lang and gender == data["gender"] and name_available == self.include_name.get(greeting, True):
                return greeting, self.include_name.get(greeting, True)
        
        # Fallback to gender-neutral greeting
        for greeting, data in self.greetings.items():
            if data["lang"] == lang and data["gender"] == "" and (name_available or not self.include_name.get(greeting, True)):
                return greeting, self.include_name.get(greeting, True)
        # If no greeting is found, return a default message
        return "Hello", name_available
