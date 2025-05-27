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
        greeting, include_name = self.get_greeting(contact, lang)
        if not include_name:
            return greeting + ","
        for token in contact.token_list:
            if token.type == TokenType.TITLE:
                greeting = greeting + " " + token.value
        for token in contact.token_list:
            if token.type == TokenType.LAST_NAME:
                greeting = greeting + " " + token.value
        greeting = greeting + ","
        return greeting 


    
    def get_greeting(self, contact: Contact, lang: Language) -> str:
        gender = contact.meta_data.gender


        for greeting, data in self.greetings.items():
            if convert_string_to_language(data["lang"]) == lang and gender == data["gender"]:
                return greeting, self.include_name.get(greeting, True)
        
        # Fallback to gender-neutral greeting
        for greeting, data in self.greetings.items():
            if data["lang"] == lang and data["gender"] == "":
                return greeting, self.include_name.get(greeting, True)
        # If no greeting is found, return a default message
        return "Hello", self.include_name.get(greeting, True)
