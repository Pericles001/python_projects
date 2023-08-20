#!usr/bin/python3
"""
Module for making requests to the online dictionary api
API url : https://api.dictionaryapi.dev/api/v2/entries/en/<word>
"""

import socket
import sys
import os

from ..a_offline_dictionary.dictionary import save_line, take_argument, search_word


def internet_checker():
    """
    Method to check if machine is connected to the internet and return True or False
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
