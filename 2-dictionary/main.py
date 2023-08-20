#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python code that simulates a dictionary based on a json file and online API.
data.json is a json file that contains a dictionary of words and their meanings.
"""

from b_online_dictionary.requests import internet_checker, \
    search_word_online
from a_offline_dictionary.dictionary import redirect_to_offline, take_argument, save_line

if __name__ == "__main__":
    save_line()
    while True:
        if internet_checker():
            target_word = take_argument("Welcome to the online dictionary. Enter a word or type 'exit' to quit:")

            if target_word.lower() == 'exit':
                print("Exiting the dictionary.")
                break

            result = search_word_online(target_word)

            if result:
                print("Definitions:")
                for meaning in result:
                    part_of_speech = meaning["partOfSpeech"]
                    print(f"{part_of_speech.capitalize()}:")

                    for definition_data in meaning["definitions"]:
                        definition = definition_data["definition"]
                        print(f" - {definition}")
            else:
                print("No definitions found online for the word. You can try searching offline.")
                redirect_to_offline()
        else:
            print("You are offline. Redirecting to offline dictionary.")
            redirect_to_offline()
