#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python code that simulates a dictionary based on a json file.
data.json is a json file that contains a dictionary of words and their meanings.
"""

from dictionary import save_line, take_argument, search_word

if __name__ == "__main__":
    """
    Main function
    """
    try:
        save_line()
        target_word = take_argument()
        print(search_word(target_word))
    except Exception as e:
        print(e)
