#!usr/bin/python3
"""
Module for making requests to the online dictionary api
API url : https://api.dictionaryapi.dev/api/v2/entries/en/<word>
"""

import socket
import sys
import os

sys.path.append("a-offline_dictionary")
# save_line = __import__('a-offline_dictionary.dictionary').save_line
take_argument = __import__('2-dictionary/a-offline_dictionary.dictionary').take_argument

take_argument()


def internet_checker():
    """
    Method to check if machine is connected to internet and return True or False
    :return: Boolean
    """
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def get_word():
    """
    Method to take a word as input and return it
    :return: String
    """
    try:
        print("Welcome to our custom dictionary.")
        print("Enter a word to get their meaning or enter 00 to exit: \n")
        target_word = input()
        return target_word.lower()
    except Exception as e:
        print(e)


def redirect_to_offline():
    """
    Method to redirect to offline dictionary
    :return:
    """
    print("You are offline. Redirecting to offline dictionary.")


take_argument()
