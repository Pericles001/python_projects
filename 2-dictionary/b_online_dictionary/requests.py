#!usr/bin/python3
"""
Module for making requests to the online dictionary api
API url : https://api.dictionaryapi.dev/api/v2/entries/en/<word>
"""

import socket

import requests



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


def search_word_online(target):
    """"
    Function that searches for a given word in online API repo and returns the definitions
   Args:
        target (str): The word to search for

    Returns:
        list: List of definitions and meanings
    """
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{target}"
    try:
        response = requests.get(api_url)
        response_data = response.json()

        if isinstance(response_data, list) and len(response_data) > 0:
            word_data = response_data[0]
            if "meanings" in word_data:
                meanings = word_data["meanings"]
                return meanings
            else:
                return []
        else:
            return []

    except requests.exceptions.RequestException as E:
        print("Error occured : " + E)
